import requests

def validate_api_key(api_key):
    """Check if the provided OpenAI API key is valid by making a test request."""
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True  # ✅ Key is valid
        elif response.status_code == 401:
            return False  # ❌ Invalid key
        else:
            return None  # ⚠️ Other status codes (e.g., rate limits, server issues)

    except Exception as e:
        print(f"Error: {str(e)}")
        return None