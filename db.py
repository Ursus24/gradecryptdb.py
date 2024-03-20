import base64
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
ENCRYPTION_KEY = b'W6k<\xb2\xa07\xae\x15\xb5\x18\xaa\x06!\xfd\x18'

def addKey(key, value):
    strKey = str(key)
    strVal = str(value)
    with open(strKey, 'w') as file:
        file.write(str(encrypt(strVal)))

def  readKey(key):
    strKey = str(key)
    if hasKey(strKey)==True:
        with open(strKey, 'r') as file:
            return decrypt(file.read())
    elif hasKey(strKey)==False:
        print("Key does not exist")
        return None
    
def addKeyUnsafe(key, value):
    strKey = str(key)
    strValue = str(value)
    with open(strKey, 'w') as file:
        file.write(strValue)

def  readKeyUnsafe(key):
    strKey = str(key)
    if hasKey(strKey)==True:
        with open(strKey, 'r') as file:
            return file.read()
    elif hasKey(strKey)==False:
        print("Key does not exist")
        return None

def deleteKey(key):
    if hasKey(key)==True:
        strKey = str(key)
        os.remove(strKey)
    elif hasKey(key)==False:
        print("Key does not exist")
        return None

def listKeys():
    return os.listdir()

def hasKey(key):
    strKey = str(key)
    if os.path.exists(strKey):
        return True
    else:
        return False

def encrypt(data):
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8') + " " + base64.b64encode(cipher.nonce).decode('utf-8')

def decrypt(data):
    data = data.split(" ")
    nonce = base64.b64decode(data[1])
    data = base64.b64decode(data[0])
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(data)
    return plaintext.decode('utf-8')

def test():
    data = "test"
    encrypted_data = encrypt(data)
    return decrypt(encrypted_data) == data