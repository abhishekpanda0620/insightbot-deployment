import requests
import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL","")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
def summarize_errors(error_text: str) -> str:
    if not error_text.strip():
        return "No significant errors found."
    
    prompt = f"Summarize and suggest fixes for these log errors:\n\n{error_text}"
    
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "").strip()
    
    except Exception as e:
        return f"AI Summary Failed: {str(e)}"
