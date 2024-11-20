import src.schemas as schemas
import src.database.requests as requests

from fastapi import APIRouter


router = APIRouter()

messages = []


@router.post('/user/add')
async def add_user(user_to_add: schemas.AddUser):
    await requests.add_user(telegram_id=user_to_add.telegram_id,
                            telegram_username=user_to_add.telegram_username)
    
    return {'status': 'ok'}


@router.post('/message/add')
async def add_message(message_to_add: schemas.AddMessage):
    user = await requests.get_user(telegram_id=message_to_add.sender_telegram_id)
    
    await requests.add_message(text=message_to_add.text,
                               user_id=user.id)
    
    return {'status': 'ok'}


@router.get('/message/get/all')
async def get_all_messages():
    messages = await requests.get_all_messages()
    
    return messages
