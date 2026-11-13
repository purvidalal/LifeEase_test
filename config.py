# config.py
# All secrets are read from environment variables. Copy .env.example to .env
# and fill in your own keys. Never commit real keys to the repository.
import os

API_KEYS = {
    "openai": os.environ.get("OPENAI_API_KEY"),
    "sarvam": os.environ.get("SARVAM_API_KEY"),
    "weather": os.environ.get("WEATHER_API_KEY"),
    "google": os.environ.get("GOOGLE_API_KEY"),
}
GOOGLE_CX = os.environ.get("GOOGLE_CX")

# Path to a sample user profile (see data/sample_profile.xlsx)
PERSONAL_INFO_PATH = os.environ.get("PERSONAL_INFO_PATH", "data/sample_profile.xlsx")
