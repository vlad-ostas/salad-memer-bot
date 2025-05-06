import asyncio

from aiogram import Router
from aiogram.types import Message


message_router = Router()


@message_router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
