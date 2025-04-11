import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

APP_CONFIG = {
    "DEBUG": os.environ['DEBUG'].lower() == "true",
    "OPENAI_API_KEY": os.environ['OPENAI_API_KEY'],
    "TRAINING_FOLDER_PATH": os.environ['TRAINING_FOLDER_PATH'],
    "CHROMA_PATH": "chroma",
    "PORT": int(os.environ.get("PORT", 3333)),
    "UI_TEMPLATE": os.environ.get("UI_TEMPLATE", 'index.html'),
    "PREDICT_RATE": float(os.environ.get("PREDICT_RATE", 0.7))
}
