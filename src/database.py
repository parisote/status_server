import motor.motor_asyncio
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGODB_URL'])
db = client[os.environ['SERVER_NAME']]
