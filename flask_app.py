from __future__ import print_function
from flask import Flask
from encryptor import RSAEncryptor
from sql_engine import SQL_Engine
import sys, uuid

my_password = b'mypassword'

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
    #the password for the serialization should be a UUID and stored in the config file.
    private_key = my_encryptor.load_private_key("rsa_private.pem", None) #this should not load from a file but instead be generated on the fly.
    s_private_key = my_encryptor.serialize_private_key(private_key, my_password)
    s_public_key = my_encryptor.serialize_public_key(my_encryptor.generate_public_key(private_key))
    a_secret_key = str(uuid.uuid4())
    
    sql_engine.create_new_identity(a_secret_key, s_public_key, s_private_key, str(uuid.uuid4()), 'test')
    f = open('config.cfg','a')
    f.write("DEBUG = True \n")
    f.write("SECRET_KEY ='" + a_secret_key + "'\n")
  
    f.close()
    attempts =+ 1

secret_key = app.config['SECRET_KEY']

from routes import *

if __name__ == '__main__' :

    app.run(debug=True)

