from sqlalchemy import select
from src.database.models import User, Message, async_session


async def add_user(telegram_id: int, telegram_username: str):
    async with async_session() as session:
        user = User(telegram_id=telegram_id, telegram_username=telegram_username)
        session.add(user)
        await session.commit()
        
        
async def get_user(telegram_id: int) -> User | None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        return user
        
        
async def add_message(text: str, user_id: int):
    async with async_session() as session:
        message = Message(text=text, user_id=user_id)
        session.add(message)
        await session.commit()


async def get_all_messages() -> list[Message]:
    async with async_session() as session:
        messages = await session.scalars(select(Message))
        return messages.all()