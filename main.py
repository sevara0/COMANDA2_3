import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("hello world")

@dp.message(Command("jardem"))
async def jardem(message:Message):
    await message.answer(f"admin @Kpakona")


async def main():
    print("bot istedi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())