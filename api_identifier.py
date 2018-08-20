from sqlalchemy import Column, String, Integer, Date

from base import Base


class Api_Identifier(Base):
    __tablename__ = 'api_identifier'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True) #id int PRIMARY KEY NOT NULL AUTO_INCREMEN
    secret_key = Column(String(2048))
    friend_code = Column(String(2048))
    name = Column(String(2048))

    def __init__(self, secret_key, friend_code, name):
        self.secret_key = secret_key
        self.friend_code = friend_code
        self.name = name
