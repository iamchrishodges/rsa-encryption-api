from flask import Flask
from encryptor import RSAEncryptor


my_encryptor = RSAEncryptor()
private_key = my_encryptor.load_private_key("rsa_private.pem", None) 


public_key = my_encryptor.generate_public_key(private_key)

app = Flask(__name__)
app.config.from_pyfile('config.py')

from routes import *

if __name__ == '__main__' :

 
    app.run(debug=True)

