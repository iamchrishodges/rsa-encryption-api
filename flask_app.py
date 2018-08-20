from __future__ import print_function  # Only needed for Python 2
from flask import Flask
from encryptor import RSAEncryptor
from sql_engine import SQL_Engine
import sys

my_pass = b'mypassword'

my_encryptor = RSAEncryptor()

sql_engine = SQL_Engine()
sql_engine.initialize()


app = Flask(__name__)

#if there's no config, create one.
attempts = 0
while not app.config.from_pyfile('config.cfg', silent=True):
    if attempts > 3:
        print('could not write config file to system.')
        sys.exit()
    
    #Need to create an RSA public Key, RSA private Key, a
    
    #create_new_identity(self, a_secret_key, a_public_key, a_private_key, a_friend_code, a_name)
    private_key = my_encryptor.load_private_key("rsa_private.pem", None)
    s_private_key = my_encryptor.serialize_private_key(private_key, my_pass)
    s_public_key = my_encryptor.serialize_public_key(my_encryptor.generate_public_key(private_key))
    
    sql_engine.create_new_identity('222222', s_public_key, s_private_key, 'bba', 'test')
    f = open('config.cfg','a')
    f.write("DEBUG = True \n")
    f.write("SECRET_KEY = '222222'\n")
    f.write("FRIEND_KEY = 'bba'\n")

    f.close()
    attempts =+ 1

private_key = my_encryptor.deserialize_private_key(sql_engine.get_private_key('222222'), b'mypassword')
public_key = my_encryptor.deserialize_public_key(sql_engine.get_public_key('bba'))

    

from routes import *

if __name__ == '__main__' :

    app.run(debug=True)

