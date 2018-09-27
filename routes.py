from flask import request, jsonify, make_response
from flask_app import app, my_encryptor, sql_engine, secret_key
from flask import render_template
import base64

error = { 'no_friend_code' : 'No friend code specified.',  'no_message' : 'Insufficient information provided to create message.', 'no_encrypted_message' : 'Insufficient information provided to decrypt message.'}
success = {'message_sent' : 'Your message has been successfully published.'}

#Get a sharable friend code
@app.route('/GetMyFriendCode/', methods = ['GET'])
def getFriendCode():
    return jsonify({ 'friend_code' : sql_engine.get_friend_code(secret_key)})


#Decrypt Messages using the known private key (loaded in at flask_app.py). These messages will be sent from a "foreign" source.
@app.route('/Decrypt/', methods=['POST'])
def decrypt():
    data = request.get_json()

    
    if 'encrypted_message' in data:
        private_key = sql_engine.get_private_key(secret_key)
        message = my_encryptor.decrypt(private_key,base64.b64decode(str(data['encrypted_message'])))
        return jsonify({'message' : message})
    else:
        return jsonify({'error' : error['no_encrypted_message']}), 400

@app.route('/PostMessage/', methods=['POST'])
def postMessage():
    my_friend_code = sql_engine.get_friend_code(secret_key) #Gets sender's friend code given their secret key. Ensures someone can't "spoof" the sender
    
    data = request.get_json()
    if 'message' and 'friend_code' in data:
        if data['friend_code']:

            friend_code = data['friend_code']
            public_key = sql_engine.get_public_key(friend_code)

            message = my_encryptor.encrypt(public_key,str(data['message']))
            encrypted_message = base64.b64encode(message)
            sql_engine.create_message(friend_code, my_friend_code, encrypted_message)
            return jsonify({'success' : success['message_sent']})
        else:
            return jsonify({'error' : error['no_friend_code']}), 400      
    else:
        return jsonify({'error' : error['no_message']}), 400

@app.route('/GetAllEncryptedMessages/', methods=['GET'])
def getAllEncryptedMessages():
    res = sql_engine.get_all_messages(secret_key)
    return jsonify(res)

@app.route('/GetAllMessages/', methods=['GET'])
def getAllMessages():
    private_key = sql_engine.get_private_key(secret_key)
    res = sql_engine.get_all_messages(secret_key)
    res = my_encryptor.decrypt_list( private_key, res)
    return jsonify(res)

@app.route('/UI/', methods=['GET'])
def ui():
     return render_template('index.html')
