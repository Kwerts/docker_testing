from pydantic import BaseModel


class Message(BaseModel):
    text: str
    sender_telegram_id: int
    
    
class AddMessage(Message):
    pass


class User(BaseModel):
    telegram_id: int
    telegram_username: str
    
    
class AddUser(User):
    pass