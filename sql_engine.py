import os
import sys
from base import Session, engine, Base
from key_pairing import Key_Pairing
from api_identifier import Api_Identifier



Base.metadata.create_all(engine)


class SQL_Engine:

    def initialize(self):
        print "Initialize Database." 
        Base.metadata.create_all(engine)
        print "Database initialized" 

    #Updates Api_Identifier and Key_Pairing tables.
    def create_new_identity(self, a_secret_key, a_public_key, a_private_key, a_friend_code, a_name):
        #Create random sender_code and random friend_code . Return these + secret_key
        kp =  Key_Pairing(a_public_key, a_private_key, a_secret_key, a_friend_code)
        ai = Api_Identifier(a_secret_key, a_friend_code, a_name)

        session = Session()
        session.add(kp)
        session.add(ai)
        session.commit()
        session.close()

    #Add a message
    def create_message(self, sender_code, friend_code, encrypted_message):
        return '2'

    #Returns a friend code for you to share with others.
    #Others can use this friend code to request your public key from database at any time.
    def get_friend_code(self, secret_key):
        return '2'

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
    eng.initialize()
    
    #eng.get_public_key('bba')
    #eng.get_private_key('222222')
