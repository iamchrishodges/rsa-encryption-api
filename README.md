# Deployment

Prerequisites
---------------
TBD

pip install flask
pip install cryptography

To Run
---------
python flask_app.py


# Overview
The RSA Encryption API demonstrates the application of RSA Encryption and how it can be used to encrypt messages stored in a database. This project allows for multiple instances of the API to be stood up and commit encrypted messages to a centralized database that can be read by a designated "friend" API.

Description of Identifiers
---------------------------
When the API is initialized, it is provided a public key, a private key, a secret key, and a "friend code" . These values are stored in a database and will be used to send messages/read messages later. 

* **Friend Code** : The "friend code" is a public string that can be given to other hostings of the API. With this friend code, a public key can be retrieved.

* **Public Key** : The public key is the part of the RSA Key pair that provides the ability to safely encrypt messages. Since the encryption algorithm is asymmetric, this key can "lock" a message but cannot "unlock" a message. In the database, this value is serialized in pem format and Base64 encoded.

* **Private Key** : The private key is the part of the RSA Key Pair that provides the ability to safely decrypt messages. Since the encryption algorithm is asymmetric, this key can "unlock" a message but cannot "lock" a message. In the database, this value is serialized in pem format with a password and Base64 encoded. The password will be stored in the config.cfg file upon API initialization.

* **Secret Key** : The secret key is the ticket to everything in this project. This is a value that will allow you to retrieve friend codes and corresponding public keys so that you may successfully send and read messages. Secret keys are registered to each API and stored in the config.cfg file. End users interacting with the API do not need to be aware of the value but, without its existence, they would not be able to read messages.


# Project Structure Summary of Files

The libraries and frameworks I utilized are phenomenal but the documentation for them were a mixed bag. As a result, I built this code highly modularized to showcase each individually so that they may be useful for applications beyond this project.

Flask App Components
---------------------
* **flask_app.py** : "Runner" for application. Includes relevant modules that will be used in a global scope.
* **routes.py** : Home for all routes for the Flask API. This separation from the flask_app is deliberate for ease of maintenance. 

SQL-Alchemy Components
------------------------
*Pure SQL-Alchemy is used in this project rather than the Flask-SQL-Alchemy framework. This allows for the code that is written to be used with other frameworks such as Pyramid.*

* **sql_engine.py** : Hosts the key queries required to initialize, read from, and write to the MySQL Database.
* **base.py** : A base model for subsequent SQL Alchemy Models.
* **api_identifier_model.py** : Not currently in use.
* **key_pairing_model.py** : A model for the key_pairing table. Contains the public key, private key, secret key, and friend code.
* **message_model.py** : A model for the message table. contains sender's friend code (my friend code), receiver's friend code (friend code), and the encrypted message.

Cryptography Components
------------------------
* **encryptor.py** : An interface that allows messages to be encrypted and decrypted easily through RSA encryption. This was built in such as way that other algorithms could be written in a similar fashion and could be swapped out with minimal rewrite required in other modules.

# Discussion

Inspiration
------------
At my day job, RSA Encryption is used to communicate messages from our application to our client's applications RESTfully. Since we're writing the messages, the encryption is handled but it's up the customer to write their decryption mechanism.  In a perfect world, these applications are all written in the same language and the tried-and-true C# samples can be ripped straight from Stack Overflow. Alas, this world is full of flaws and pariah cults of Linux developers still lurk in the shadows that shun .Net Communication. A (surprisingly) misunderstood algorithm was certainly salt in the wound.

My goal was first to describe the handshake to developers and their requirements to meet our applicaiton's standards; after explaining it 900 times, I decided to implement it one weekend and the encryptor module was born. Later, I revisted the project and wrapped it all in a Flask app and threw in SQL Alchemy for the fun of it.


Potential Pitfalls of the Project
----------------------------------

RSA Encryption is a solid choice that can almost guarantee security but the algorithm is slow and is often used to encrypt small chunks of information that usually does not persist. In scenarios where data does not persist, keys can be swapped out at will further strengthening a systems' security.

In this project, APIs create new key sets upon initialization whenever a config.cfg file does not exist. Since the encrypted messages persist, the keys for these APIs must stay the same if older messages are to be archived or a mechanism must be created for a key history.

Additionally, this project assumes that two applications have access to a unified database that would provide them with the public and private keys of similar applications. Private keys are password-protected and never stored in a unified location but, with the current implementation, there's no way to update this password for padded security. As an extension to this project, the paradigm could be re-sculpted where Users within a single application have access to this singular database and the users can utilize RSA to send messages to each other instead of entire applications.
