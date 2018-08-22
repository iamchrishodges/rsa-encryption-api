from flask import request, jsonify, make_response
from flask_app import app, my_encryptor, sql_engine, public_key, private_key, secret_key
import base64

error = { 'no_message' : 'Insufficient information provided to create message.', 'no_encrypted_message' : 'Insufficient information provided to decrypt message.'}
success = {'message_sent' : 'Your message has been successfully published.'}
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

@app.route('/PostMessage/', methods=['POST'])
def postMessage():
    my_friend_code = sql_engine.get_friend_code(secret_key) #Gets sender's friend code given their secret key. Ensures someone can't "spoof" the sender

    data = request.get_json()
    if 'message' and 'friend_code' in data:
        friend_code = data['friend_code']
        message = my_encryptor.encrypt(public_key,str(data['message']))
        encrypted_message = base64.b64encode(message)
        sql_engine.create_message(friend_code, my_friend_code, encrypted_message)
        return jsonify({'success' : success['message_sent']})
    else:
        return jsonify({'error' : error['no_message']})

@app.route('/GetAllEncryptedMessages/', methods=['GET'])
def getMessages():
    res = sql_engine.get_all_messages(secret_key)
    
    return jsonify(res)