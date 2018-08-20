import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Table, MetaData

conn_string ='mysql+mysqldb://root:test123@localhost:3306/rsa_unified_db'
engine = create_engine(conn_string, pool_recycle=3600)

Base = declarative_base()
metadata = MetaData(engine)

class SQL_Engine:

    def connect(self, connection_string):
        self.conn_string = connection_string
    
    def initialize(self):

        if not self.check_for_tables(['api_identifier','key_pairing', 'message', 'sender']):
            Base = declarative_base()
            
            class Api_Identifier(Base):
                __tablename__ = 'api_identifier'

                id = Column(Integer, primary_key=True)
                secret_key = Column(String(250))
                friend_code = Column(String(250))
                sender_code = Column(String(250))
                name = Column(String(250))
                
            class Key_Pairing(Base):
                __tablename__ = 'key_pairing'

                id = Column(Integer, primary_key=True)
                public_key = Column(String(250))
                private_key = Column(String(250))
                secret_key = Column(String(250))
                friend_code = Column(String(250))
                
            class Message(Base):
                __tablename__ = 'message'

                id = Column(Integer, primary_key=True)
                sender_code = Column(String(250))
                friend_code = Column(String(250))
                message = Column(String(250))

            class Sender(Base):
                __tablename__ = 'sender'

                id = Column(Integer, primary_key=True)
                sender_code = Column(String(250))
                name = Column(String(250))

            Base.metadata.create_all(engine)

            print "Database initialized" 
        else:
            print "Database already populated"     

        self.create_tables()

    def check_for_tables(self, table_list):
        for table in table_list:
            if not engine.dialect.has_table(engine, table):
                return False
        return True

    def create_tables(self):
        self.api_identifier = Table('api_identifier', metadata,    
            Column('id', Integer, primary_key=True),
            Column('secret_key', String(250)),
            Column('friend_code', String(250)),
            Column('sender_code', String(250)),
            Column('name', String(250)), 
            extend_existing=True)

        self.key_pairing = Table('key_pairing', metadata,    
            Column('id', Integer, primary_key=True),
            Column('public_key', String(250)),
            Column('private_key', String(250)),
            Column('secret_key', String(250)),
            Column('friend_code', String(250)), 
            extend_existing=True)   

        self.message = Table('message', metadata,    
            Column('id', Integer, primary_key=True),
            Column('sender_code', String(250)),
            Column('friend_code', String(250)),
            Column('message', String(250)), 
            extend_existing=True)

        self.sender = Table('sender', metadata,    
            Column('id', Integer, primary_key=True),
            Column('sender_code', String(250)),
            Column('name', String(250)),
            Column('message', String(250)), 
            extend_existing=True)

    #Updates Api_Identifier and Key_Pairing tables.
    def crate_new_identity(self, a_secret_key, a_public_key, a_private_key):
        #Create random sender_code and random friend_code . Return these + secret_key

        ins = self.api_identifier.insert().values(
            id = 3,
            secret_key = a_secret_key ,
            
            friend_code = '2',
            sender_code = '3',
            name = '4'
        )
        conn = engine.connect()
        conn.execute(ins)
    #Add a message
    def create_message(self, sender_code, friend_code, encrypted_message):
        return '2'

    #Returns a friend code for you to share with others.
    #Others can use this friend code to request your public key from database at any time.
    def get_friend_code(self, secret_key):
        return '2'

    #Request a public key so you can begin sending messages to a friend.
    def get_public_key(self, friend_code):
        return '1'

    #The Secrect Key is something only you should be aware of
    def get_private_key(self, secret_key):
        return '1'

    #Get name given sneder_id
    def get_name(self, sender_code):
        return '1'

    #With known friend code, get all encryted messages.
    #Someone could potentially try to use this maliciously and hack their API
    #The result would be a dict of encrypted strings (not very useful for them)
    def get_all_messages(self, friend_code):
        return '1'    



if __name__ == '__main__':

    eng = SQL_Engine()
    eng.connect('mysql+mysqldb://root:test123@localhost:3306/rsa_unified_db')
    eng.initialize()

    eng.crate_new_identity('1', '2', '3')