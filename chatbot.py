import openai
import json
import os
import config  # Importing configuration file
from google.cloud import translate_v2 as translate

# Load API Keys Securely
openai.api_key = os.getenv("OPENAI_API_KEY", config.OPENAI_API_KEY)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Micha/MHChatGPT/gpt-psychiatry-80a38e829ff7.json"

# Initialize Google Translation Client
translate_client = translate.Client()

def detect_language(text):
    """Detects the language of the input text."""
    result = translate_client.detect_language(text)
    return result["language"]

def translate_text(text, target_language):
    """Translates text into the target language."""
    if target_language == "en":
        return text  # No need to translate if it's already in English
    result = translate_client.translate(text, target_language=target_language)
    return result["translatedText"]

def chatbot_response(user_input, user_language="en"):
    """Handles mhChatGPT development logic with optimized translation support."""
    
    # Step 1: Detect Language Automatically
    detected_lang = detect_language(user_input)
    if detected_lang != "en" and detected_lang in config.SUPPORTED_LANGUAGES:
        user_language = detected_lang
    
    # Step 2: Detect Language Switch Command
    if user_input.startswith("/lang "):
        new_lang = user_input.split("/lang ")[-1].strip()
        if new_lang in config.SUPPORTED_LANGUAGES:
            return f"Language switched to {new_lang.upper()}!"
        return "Unsupported language. Please choose from supported languages."
    
    # Step 3: Handle Greeting Translation Requests
    if "say " in user_input.lower() and "in" in user_input.lower():
        parts = user_input.lower().split(" in ")
        if len(parts) == 2:
            phrase, target_lang = parts
            target_lang = target_lang.strip().lower()
            if target_lang in config.LANGUAGE_CODES:
                return translate_text(phrase.replace("say ", ""), config.LANGUAGE_CODES[target_lang])
            else:
                return "Sorry, I do not support that language."
    
    # Step 4: Identify Development Needs
    user_input_lower = user_input.lower()
    
    if "debug" in user_input_lower:
        response = "What specific error or issue are you facing?"
    elif "optimize" in user_input_lower:
        response = "Would you like help with performance, security, or scalability improvements?"
    elif "wordpress" in user_input_lower:
        response = "Are you looking to integrate mhChatGPT as a plugin or via API in WordPress?"
    elif "deploy" in user_input_lower:
        response = "Would you like guidance on cloud hosting, local hosting, or API deployment?"
    elif "api" in user_input_lower:
        response = "Do you need help with API authentication, request handling, or response formatting?"
    else:
        # Default AI Response with concise output
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": config.SYSTEM_PROMPT},
                      {"role": "user", "content": user_input}]
        )["choices"][0]["message"]["content"]
    
    # Step 5: Translate Response if Necessary
    if user_language != "en":
        response = translate_text(response, user_language)
    
    return response

# Run chatbot in a loop
print("mhChatGPT Development Assistant 🛠️ (Type 'exit' to quit)")
user_language = "en"  # Default language
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        break
    if user_message.startswith("/lang "):
        user_language = user_message.split("/lang ")[-1].strip()
        print(f"Chatbot: Language switched to {user_language.upper()}!")
        continue
    print("Chatbot:", chatbot_response(user_message, user_language))
