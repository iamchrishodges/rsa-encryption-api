import os
import sys
import decimal, datetime, json
from base import Session, engine, Base
from key_pairing_model import Key_Pairing
from api_identifier_model import Api_Identifier
from message_model import Message, MessageSchema


Base.metadata.create_all(engine)

message_schema = MessageSchema()

class SQL_Engine:
    
    def initialize(self):
        Base.metadata.create_all(engine)
        print "Database initialized" 

    #Updates Api_Identifier and Key_Pairing tables.
    def create_new_identity(self, a_secret_key, a_public_key, a_private_key, a_friend_code, a_name):
        #ToDo: Create random sender_code and random friend_code . Return these + secret_key
        kp =  Key_Pairing(a_public_key, a_private_key, a_secret_key, a_friend_code)
        ai = Api_Identifier(a_secret_key, a_friend_code, a_name)
        self.update_statement([kp, ai])
        return True

    #Add a message
    def create_message(self, a_friend_code,  a_my_friend_code, a_encrypted_message):
        m = Message(a_friend_code, a_my_friend_code, a_encrypted_message)
        self.update_statement([m])
        return True

    #Returns a friend code for you to share with others.
    #Others can use this friend code to request your public key from database at any time.
    def get_friend_code(self, a_secret_key):
        session = Session()
        res = session.query(Key_Pairing.friend_code).filter(Key_Pairing.secret_key == a_secret_key).first()
        session.close()
        return res[0]


    #Request a public key so you can begin sending messages to a friend.
    def get_public_key(self, a_friend_code):
        session = Session()
        res = session.query(Key_Pairing.public_key).filter(Key_Pairing.friend_code == a_friend_code).first()
        session.close()
        return res[0]

    #The Secrect Key is something only you should be aware of
    def get_private_key(self, a_secret_key):
        session = Session()
        res = session.query(Key_Pairing.private_key).filter(Key_Pairing.secret_key == a_secret_key).first()
        session.close()
        return res[0]

    #Someone could potentially try to use this maliciously and hack their API
    #The result would be a dict of encrypted strings (not very useful for them)
    def get_all_messages(self, a_secret_key):
        a_my_friend_code = self.get_friend_code(a_secret_key)
        session = Session()
        res = session.query(Message.friend_code, Message.my_friend_code, Message.message).filter(Message.my_friend_code == a_my_friend_code)
        session.close()
        ret = []
        for e in res:
            m = message_schema.dump(e).data
            ret.append(m)
        return ret

    def update_statement(self, model_list):
        session = Session()
        for model in model_list:
            session.add(model)
        session.commit()
        session.close()
 

if __name__ == '__main__':

    eng = SQL_Engine()
    #eng.initialize()
    print eng.get_all_messages('222222')
    #eng.get_public_key('bba')
    #eng.get_private_key('222222')
