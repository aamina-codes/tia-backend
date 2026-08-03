import os

from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# ==========================
# API Keys
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================
# AI Models
# ==========================

DEFAULT_PROVIDER = "gemini"

from config.settings import GEMINI_MODEL

# ==========================
# Project Folders
# ==========================

from config.settings import UPLOAD_FOLDER

folder = UPLOAD_FOLDER

EXTRACTED_TEXT = "extracted_text"

EXTRACTED_JSON = "extracted_json"

OUTPUT_FOLDER = "output"

DATASET_FOLDER = "dataset"

LOGS_FOLDER = "logs"

TEMP_FOLDER = "temp"

from config.settings import MAX_RETRIES