from sqlalchemy import Column, String, Integer, Date

from base import Base

class Key_Pairing(Base):
    __tablename__ = 'key_pairing'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    public_key = Column(String(2048))
    private_key = Column(String(2048))
    secret_key = Column(String(2048))
    friend_code = Column(String(2048))

    def __init__(self, public_key, private_key, secret_key, friend_code):

        self.public_key = public_key
        self.private_key = private_key
        self.secret_key = secret_key
        self.friend_code = friend_code