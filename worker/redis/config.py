import aioredis
from dotenv import load_dotenv
import os

load_dotenv()

class Redis:
    def __init__(self):
        self.User = os.getenv("REDIS_USER")
        self.Password = os.getenv("REDIS_PASSWORD")
        self.Url = os.getenv("REDIS_URL")

        self.connection_url = f"redis://{self.User}:{self.Password}@{self.Url}"
    
    async def create_connection(self):
        self.connection = aioredis.from_url(self.connection_url, db=0)

        return self.connection