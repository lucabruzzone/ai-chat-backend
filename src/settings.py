from os import getenv as env

# pylint: disable=import-error
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = str(env("OPENAI_API_KEY", default=""))
PORT = int(env("PORT", default="500"))
