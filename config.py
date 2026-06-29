from google import genai
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()
# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "gemini-3-pro-preview"
# -----------------------------
# Gemini Client
# -----------------------------
CLIENT = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)