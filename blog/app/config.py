import os
from dotenv import load_dotenv
import datetime

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
