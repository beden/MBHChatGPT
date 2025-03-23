# config.py - Configuration file for mhChatGPT

# OpenAI API Key (Ensure this is set before running the chatbot)
OPENAI_API_KEY = "REDACTED"

# Google Cloud Translation API Key (Path to credentials JSON file)
GOOGLE_APPLICATION_CREDENTIALS = "C:/Users/Micha/MHChatGPT/gpt-psychiatry-80a38e829ff7.json"

# System Prompt for Chatbot Behavior
SYSTEM_PROMPT = """
You are mhChatGPT, a development assistant for chatbot debugging, optimization, and deployment.
Your role is to:
1️⃣ Help refine chatbot logic and responses.
2️⃣ Assist in API integration, WordPress deployment, and performance tuning.
3️⃣ Ensure structured, clear, and professional chatbot interactions.

⚠️ **Rules:**
- Do not provide medical advice.
- Do not diagnose or suggest treatments.
- Only assist in chatbot development and deployment.
"""

# List of supported languages for translation
SUPPORTED_LANGUAGES = ["en", "es", "he", "ja", "hi", "ru", "fr", "zh", "de", "it", "ar", "el"]

# Mapping of language names to language codes
LANGUAGE_CODES = {
    "english": "en",
    "spanish": "es",
    "hebrew": "he",
    "japanese": "ja",
    "hindi": "hi",
    "russian": "ru",
    "french": "fr",
    "chinese": "zh",
    "german": "de",
    "italian": "it",
    "arabic": "ar",
    "greek": "el"
}