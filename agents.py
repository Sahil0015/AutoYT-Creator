from crewai import Agent
import os
from style_helper import format_style_description

def yt_agent(yt_tool, api_key, video_title):
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    ytagent = Agent(
        role="YouTube Researcher",
        goal=(
            f"""Analyze the YouTube video titled '{video_title}'. Extract key sections, summarize important points, and highlight critical insights. """
        ),
        tools=[yt_tool],
        backstory=(
            """As a seasoned YouTube content analyst, you specialize in watching individual videos and summarizing key points. You structure in bullet points and critical insights."""
        ),
        verbose=True,
        max_iter = 1,
        memory=False,
        allow_delegation=True
    )

    return ytagent



def blog_writer(selected_tool, api_key, blog_topic, source_type, content_styles, content_length):
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    # Format styles
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "default informative style"

    agent = Agent(
        role="Writer & Editor",
        goal=(
            f"Write and polish a high-quality blog post on the topic '{blog_topic}' using insights from {source_type}. "
            f"Adapt the writing to match the selected tone and styles: {styles_text} ({style_description}). "
            f"Ensure the blog post is well-structured, engaging, and matches the required length: {content_length}. "
            "After drafting, thoroughly edit the content to improve grammar, sentence structure, coherence, and clarity. "
            "Eliminate redundancy and ensure the final piece is polished, professional, and reader-friendly."
        ),
        backstory=(
            "You are an AI with dual expertise in writing and editing blog content. "
            "You synthesize insights from sources like YouTube videos, articles, and PDFs to draft content, "
            "and then act as an editor to refine the same. Your talent lies in crafting content that balances "
            "tone, length, engagement, and accuracy."
        ),
        tools=[selected_tool],  # Source tool for gathering info (web, YouTube, PDF, etc.)
        verbose=True,
        max_iter=1,
        memory=False,
        allow_delegation=False
    )

    return agent



def social_media_agent(selected_tool, api_key, platform, content_styles):
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    # Ensure content styles are formatted properly
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "default engaging style"

    sm_agent = Agent(
        role="Social Media Strategist",
        goal=(
            f"Create an engaging and platform-optimized social media post for {platform}. "
            f"The content should align with the selected styles: {styles_text} ({style_description}). "
            "Ensure the post follows the best engagement practices for this platform, "
            "including formatting, tone, and strategic use of hashtags and emojis where applicable."
            "When you're done, write your final answer directly."
        ),
        verbose=True,
        memory=False,
        backstory=(
            f"You are a highly skilled social media strategist, specializing in crafting content for {platform}. "
            "Your expertise lies in understanding audience behavior, platform algorithms, and viral trends. "
            "You tailor content to maximize engagement, ensuring each post resonates with its intended audience."
        ),
        tools=[selected_tool],
        max_iter=1,
        allow_delegation=False
    )

    return sm_agent


def summarizer_agent(selected_tool, api_key, content_styles, summary_length):
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    # Format styles
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "clear and concise"

    summarizer = Agent(
        role="Content Summarizer",
        goal=(
            f"Generate a {summary_length}-length summary that is {style_description}. "
            "Summarize the input material while retaining its core message and structure."
        ),
        backstory=(
            "You are a highly intelligent summarization expert trained to extract meaningful insights from long texts, "
            "multimedia transcripts, and web articles. Your goal is to make content digestible and accessible, "
            f"while adapting to the {style_description} needs of your users."
        ),
        tools=[selected_tool],
        max_iter=1,
        verbose=True,
        memory=False,
        allow_delegation=False
    )

    return summarizer


def email_generator_agent(selected_tool, api_key, email_purpose, recipient_type, content_styles, tone="professional"):
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

    # Format styles
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else tone

    email_agent = Agent(
        role="Email Writer",
        goal=(
            f"Write a {tone} email for the purpose: '{email_purpose}', tailored to a {recipient_type}. "
            f"The email must be styled as {style_description}, ensuring clarity, relevance, and appropriate structure."
        ),
        backstory=(
            f"You specialize in writing impactful emails, whether formal or informal, for different purposes like job applications, "
            "follow-ups, business pitches, or casual updates. Your writing reflects empathy, clarity, and purpose."
        ),
        tools=[selected_tool],
        verbose=True,
        max_iter=1,
        memory=False,
        allow_delegation=False
    )

    return email_agent

