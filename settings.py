import os
from dotenv import load_dotenv


load_dotenv()


PORT = int(os.getenv("PORT"))
BASE_PATH = os.getenv("BASE_PATH")
HOT_RELOAD = os.getenv("HOT_RELOAD").lower() == "true"

LINE_CH_SECRET = os.getenv("LINE_CH_SECRET")
LINE_CH_ACCESS_TOKEN = os.getenv("LINE_CH_ACCESS_TOKEN")

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
