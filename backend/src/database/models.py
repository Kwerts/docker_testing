import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, ForeignKey


load_dotenv()

engine = create_async_engine(url='database')

async_session = async_sessionmaker(bind=engine)


class Base(DeclarativeBase):
    id: Mapped[int] =  mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"
    
    telegram_id = mapped_column(BigInteger, unique=True)
    telegram_username: Mapped[str] = mapped_column()


class Message(Base):
    __tablename__ = "messages"
    
    text: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


async def create_database_and_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)