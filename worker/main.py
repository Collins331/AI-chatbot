from redis.config import Redis
import asyncio

async def main():
    redis = Redis()
    redis = await redis.create_connection()
    print(redis)
    redis.set("name", "Collins")


if __name__ == "__main__":
    asyncio.run(main())