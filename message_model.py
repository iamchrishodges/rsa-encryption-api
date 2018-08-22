from sqlalchemy import Column, String, Integer, Date
from marshmallow_sqlalchemy import ModelSchema
from base import Base

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    my_friend_code = Column(String(2048))
    friend_code = Column(String(2048))
    message = Column(String(2048))

    def __init__(self, friend_code, my_friend_code, message):
        self.my_friend_code = my_friend_code
        self.friend_code = friend_code
        self.message = message

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}    

class MessageSchema(ModelSchema):
    class Meta:
        model = Message
