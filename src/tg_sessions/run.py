import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.config import settings

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

async def main():
    # dp.include_router()
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")