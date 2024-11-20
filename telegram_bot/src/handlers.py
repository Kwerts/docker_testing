import aiohttp

from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def any_message_echo(message: Message):
    data = {
        'text': message.text,
        'sender_telegram_id': message.from_user.id,
        }
    async with aiohttp.ClientSession() as session:
        async with session.post('http://backend:8000/message/add', json=data) as response:
            print(response.status)
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://backend:8000/message/get/all') as response:
            message_to_user = str(await response.json())
    
    await message.answer(text=message_to_user)
