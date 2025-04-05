# style_helper.py

# Function to format selected content styles into a readable string
def format_style_description(styles):
    """
    Converts a list of selected content styles into a descriptive string.

    Parameters:
    styles (list): A list of user-selected content styles (e.g., ["Casual", "Engaging", "Humorous"]).

    Returns:
    str: A formatted string describing the selected styles.
    """
    
    # Predefined content style descriptions
    STYLE_DESCRIPTIONS = {
        "Casual": "relaxed, conversational, and friendly",
        "Formal": "structured, respectful, and polished",
        "Professional": "clear, authoritative, and well-structured",
        "Engaging": "interactive, audience-focused, and dynamic",
        "Persuasive": "convincing, emotionally appealing, and impactful",
        "Humorous": "witty, playful, and fun",
        "Inspirational": "uplifting, motivational, and encouraging",
        "Technical": "precise, detail-oriented, and expert-level",
        "Minimalist": "short, direct, and concise",
        "Storytelling": "narrative-driven, engaging, and compelling",
        "Educational": "instructive, explanatory, and informative",
        "Informative": "fact-based, clear, and objective",
        "Witty": "clever, humorous, and sharp",
        "Analytical": "data-driven, critical, and evaluative",
        "Conversational": "casual, personable, and dialogue-oriented",
        "Critical": "evaluative, thoughtful, and discerning",
        "Empathetic": "understanding, compassionate, and emotionally aware"
    }

    # Generate descriptions for selected styles
    descriptions = [STYLE_DESCRIPTIONS[style] for style in styles if style in STYLE_DESCRIPTIONS]

    # Join the descriptions in a readable format
    return " and ".join(descriptions)