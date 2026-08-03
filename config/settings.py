"""
Application Configuration

Centralized configuration for the entire backend.
"""

from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploaded_reports"

OUTPUT_FOLDER = BASE_DIR / "output"

EXTRACTED_JSON_FOLDER = BASE_DIR / "extracted_json"

EXTRACTED_TEXT_FOLDER = BASE_DIR / "extracted_text"

LOG_FOLDER = BASE_DIR / "logs"

TEMP_FOLDER = BASE_DIR / "temp"

MODELS_FOLDER = BASE_DIR / "models"

# ==========================================================
# AI Configuration
# ==========================================================

AI_PROVIDER = "Gemini"

GEMINI_MODEL = "gemini-2.5-flash"

MAX_RETRIES = 3

# ==========================================================
# File Upload Configuration
# ==========================================================

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg"
}

MAX_FILE_SIZE_MB = 20

# ==========================================================
# History Configuration
# ==========================================================

HISTORY_LIMIT = 100

ENABLE_HISTORY = True

# ==========================================================
# Logging
# ==========================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOG_FOLDER / "app.log"

# ==========================================================
# API
# ==========================================================

API_TITLE = "TIA Backend API"

API_VERSION = "1.0.0"

API_DESCRIPTION = (
    "Thyroid Intelligent Assistant Backend"
)

# ==========================================================
# Ensure Required Directories Exist
# ==========================================================

DIRECTORIES = [

    UPLOAD_FOLDER,

    OUTPUT_FOLDER,

    EXTRACTED_JSON_FOLDER,

    EXTRACTED_TEXT_FOLDER,

    LOG_FOLDER,

    TEMP_FOLDER,

    MODELS_FOLDER

]

for directory in DIRECTORIES:

    directory.mkdir(
        parents=True,
        exist_ok=True
    )