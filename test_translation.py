import os
from google.cloud import translate_v2 as translate

# ✅ Force the correct credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Micha/MHChatGPT/gpt-psychiatry-80a38e829ff7.json"

# ✅ Initialize Google Translation Client
translate_client = translate.Client()

# ✅ Test translation (English to Spanish)
text = "Hello, how are you?"
target_language = "es"

result = translate_client.translate(text, target_language=target_language)
print("✅ Translation API is working!")
print(f"Original: {text}")
print(f"Translated: {result['translatedText']}")
