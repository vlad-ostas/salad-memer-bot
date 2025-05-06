import asyncio
import logging
import sys
from dotenv import load_dotenv, dotenv_values
import os 

from aiogram import Bot, Router, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from message_router import message_router


load_dotenv()
TOKEN = os.getenv("SALAD_BOT_TOKEN")


dp = Dispatcher()
dp.include_router(message_router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

