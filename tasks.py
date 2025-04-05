from crewai import Task
from style_helper import format_style_description

def create_yt_tasks(yt_agent):
    yt_task = Task(
        description=(
            f"""Analyze the Youtube Video. Extract key sections, summarize important points, and highlight critical insights. """
        ),
        expected_output=(
            f"""Extracting the key insights from the video provided"""
        ),
        tools=yt_agent.tools,
        async_execution=False,
        agent=yt_agent
    )
    return yt_task



def create_blog_task(agent, blog_topic, source_type, content_styles, content_length, task_type):
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "default professional tone"

    task = Task(
        description=(
            f"Create a well-structured and high-quality blog post on the topic '{blog_topic}', using {source_type} as the primary source. "
            f"Apply the following tone and style: {styles_text} ({style_description}), and ensure the length matches the requirement: {content_length}. "
            "Structure the blog in the following format:\n\n"
            "1. **Title** – Catchy and relevant to the topic.\n"
            "2. **Introduction** – Briefly introduce the topic and hook the reader.\n"
            "3. **Main Body** – Organize with meaningful subheadings (H2s/H3s), include examples, data, or bullet points where necessary.\n"
            "4. **Conclusion** – Summarize key takeaways and optionally suggest next steps or include a CTA.\n"
            "5. **Call-to-Action** – Encourage the reader to take a specific action (comment, share, follow, etc.).\n\n"
            "After writing, edit the blog post for grammar, coherence, and clarity. Ensure it is polished, professional, and easy to read."
        ),
        expected_output=(
            "A structured, engaging, and polished blog post with:\n"
            "- A compelling **Title**\n"
            "- An informative **Introduction**\n"
            "- A **Main Body** divided by relevant subheadings\n"
            "- A clear and concise **Conclusion**\n"
            "- An effective **Call-to-Action**\n\n"
            f"The tone should follow: {styles_text}. The content must be edited for readability and match the desired length: {content_length}."
        ),
        tools=agent.tools,
        async_execution=False,
        context=[task_type],
        agent=agent
    )

    return task



def create_social_task(social_media_agent, platform, topic, content_styles, content_length, task_type):
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "default engaging tone"

    platform_tips = {
        "Twitter": "Keep it under 280 characters, include 1-2 hashtags, emojis are fine, use a strong hook.",
        "LinkedIn": "Professional tone, use line breaks for readability, include a CTA or question to encourage engagement.",
        "Instagram": "Friendly tone, use hashtags and emojis, format for mobile reading, optionally add a short caption.",
        "Facebook": "Use conversational tone, 1-3 sentences with a clear message, emojis and links are okay.",
        "Reddit": "Informative or discussion-driven tone, avoid marketing language, format clearly with headings or bullet points, and keep it subreddit-appropriate."
    }
    platform_guidelines = platform_tips.get(platform, "Follow best practices for structure, tone, and formatting.")

    social_task = Task(
        description=(
            f"Craft a platform-optimized social media post for **{platform}** based on the topic: '{topic}'.\n\n"
            f"- Style: {styles_text} ({style_description})\n"
            f"- Length: {content_length}\n"
            f"- Platform Guidelines: {platform_guidelines}\n\n"
            "Make the post engaging, structured, and aligned with the platform's best practices. "
            "Include appropriate formatting, hashtags, mentions, emojis (if applicable), and an effective call-to-action if suitable."
        ),
        expected_output=(
            f"A polished and platform-appropriate social post for {platform} on the topic '{topic}',\n"
            f"written in a {styles_text} tone, optimized for {content_length} length.\n"
            "The post should:\n"
            "- Start with a hook or relevant question\n"
            "- Be readable and scannable\n"
            "- Follow community or platform tone rules\n"
            "- Optionally include hashtags or references if appropriate"
        ),
        tools=social_media_agent.tools,
        async_execution=False,
        context=[task_type],
        agent=social_media_agent
    )

    return social_task




def create_summary_task(summarizer_agent, source_type, content_styles, summary_length, task_type):
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else "clear and concise"

    task = Task(
        description=(
            f"Summarize content from the provided {source_type}. "
            f"The summary should be {summary_length} in length and written in a {styles_text} tone ({style_description}). "
            "Focus on key takeaways, structure, clarity, and readability."
        ),
        expected_output=(
            f"A {summary_length} summary of the {source_type} content that clearly communicates the main ideas, "
            f"is written in a {styles_text} tone, and is easy to read and understand."
        ),
        tools=summarizer_agent.tools,
        async_execution=False,
        context=[task_type],
        agent=summarizer_agent
    )

    return task




def create_email_task(email_agent, email_purpose, recipient_type, content_styles, tone, task_type):
    style_description = format_style_description(content_styles)
    styles_text = ", ".join(content_styles) if content_styles else tone

    task = Task(
        description=(
            f"Write an email with the purpose: '{email_purpose}', addressed to a {recipient_type}. "
            f"The tone should be {tone} and the content should follow these styles: {styles_text} ({style_description}). "
            "The email should include a clear subject line, proper structure (greeting, body, closing), and align with professional standards."
        ),
        expected_output=(
            f"A well-structured and polished email for '{email_purpose}', written to a {recipient_type} in a {styles_text} tone. "
            "It should include a subject line, greeting, body, and closing, while maintaining clarity, coherence, and tone alignment."
        ),
        tools=email_agent.tools,
        async_execution=False,
        context=[task_type],
        agent=email_agent
    )

    return task
