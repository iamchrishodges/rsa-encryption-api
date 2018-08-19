from flask import request, jsonify, make_response
from flask_app import app, my_encryptor, public_key, private_key
import base64

error = { 'no_message' : 'Insufficient information provided to create message.', 'no_encrypted_message' : 'Insufficient information provided to decrypt message.'}

#Encrypt Messages using the known public key (loaded in at flask_app.py)
@app.route('/EncryptFamiliarMessage/', methods=['POST'])
def encrypt():
    data = request.get_json()
    if 'message' in data:
        message = my_encryptor.encrypt(public_key,str(data['message'])) #For now, this logic will do. We will actually make this a request to foreign server later.
        return jsonify({'encrypted_message' : base64.b64encode(message)})
    else:
        return jsonify({'error' : error['no_message']})    

#Decrypt Messages using the known private key (loaded in at flask_app.py). These messages will be sent from a "foreign" source.
@app.route('/DecryptForeignMessage/', methods=['POST'])
def decrypt():
    data = request.get_json()
    if 'encrypted_message' in data:
        message = my_encryptor.decrypt(private_key,base64.b64decode(str(data['encrypted_message'])))
        return jsonify({'message' : message})
    else:
        return jsonify({'error' : error['no_encrypted_message']})