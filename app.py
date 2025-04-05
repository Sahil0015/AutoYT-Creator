import streamlit as st
import os
from crewai import Crew, Process
from api_key_validation import validate_api_key
from agents import (yt_agent, blog_writer, social_media_agent, summarizer_agent, email_generator_agent)
from tasks import (create_yt_tasks, create_blog_task, create_social_task, create_summary_task, create_email_task)
from tools import create_yt_tool

# Streamlit App
st.set_page_config(page_title="Autonomous AI Content Creator", page_icon="🦜")
st.title("Autonomous AI Content Creator")

api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key.strip():
    st.warning("Please enter your OpenAI API key.")
    st.stop()

if validate_api_key(api_key) is not True:
    st.error("❌ Invalid OpenAI API key. Please enter a valid key.")
    st.stop()

os.environ["OPENAI_API_KEY"] = api_key
st.success("✅ API key is valid.")

source_type = st.radio(
    "Choose your source type:",
    options=["YouTube"],
    horizontal=True,
    index=0
)

Output = st.selectbox("Select the output type", ["Blog", "Social Media Post", "Summary", "Email"])

context_length = st.selectbox("Desired content length", ["Short", "Medium", "Long"])

context_style = st.multiselect(
    "Choose one or more context styles:",
    options=[
        "Casual", "Formal", "Professional", "Engaging", "Persuasive",
        "Humorous", "Inspirational", "Technical", "Minimalist", "Storytelling",
        "Educational", "Informative", "Witty", "Analytical", "Conversational",
        "Critical", "Empathetic"
    ]
)

st.markdown("---")

if source_type == "YouTube":
    channel_handle = st.text_input(f"Enter the YT channel for which you want to generate {Output}")
    video_title = st.text_input("Enter the video title")

    if channel_handle and video_title:
        yt_tool = create_yt_tool(channel_handle)
        ytagent = yt_agent(yt_tool, api_key, video_title)
        yt_task = create_yt_tasks(ytagent)

        output_agents = []
        output_tasks  = []

        if Output == "Blog":
            blogwriter = blog_writer(yt_tool, api_key, video_title, source_type ,context_style, context_length)
            blog_task = create_blog_task(blogwriter, video_title, source_type, context_style, context_length, yt_task)
            output_agents.append(blogwriter)
            output_tasks.append(blog_task)

        elif Output == "Social Media Post":
            platform = st.selectbox(
                "Select the platform for posting",
                ["LinkedIn", "Twitter", "Instagram", "Facebook", "Reddit"]
            )
            sm_agent = social_media_agent(yt_tool, api_key, platform, context_style)
            sm_task = create_social_task(sm_agent, platform, video_title, context_style, context_length, yt_task)
            output_agents.append(sm_agent)
            output_tasks.append(sm_task)

        elif Output == "Summary":
            summary_agent = summarizer_agent(yt_tool, api_key, context_style, context_length)
            summary_task = create_summary_task(summary_agent, source_type, context_style, context_length, yt_task)
            output_agents.append(summary_agent)
            output_tasks.append(summary_task)

        elif Output == "Email":
            recipient_type = st.text_input("Enter the recipient type (e.g., friend, colleague, client)")
            email_purpose  = st.text_input("Enter the purpose of the email")
            email_agent_obj = email_generator_agent(yt_tool, api_key, email_purpose, recipient_type, context_style)
            email_task = create_email_task(email_agent_obj, email_purpose, recipient_type, context_style, "professional", yt_task)
            output_agents.append(email_agent_obj)
            output_tasks.append(email_task)

        if st.button(f"Generate {Output}"):
            crew = Crew(
                agents=[ytagent] + output_agents,
                tasks=[yt_task] + output_tasks,
                process=Process.sequential,
                memory=False,
                cache=True,
                share_crew=True,
                max_rpm=100,
                verbose=False
            )
            result = crew.kickoff(inputs={"video_title": video_title})
            st.success(f"{Output} generation completed!")
            st.subheader(f"📄 Generated {Output}")
            st.markdown(result.raw)
