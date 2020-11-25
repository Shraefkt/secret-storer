from cryptography.fernet import Fernet
key = b'sfGsPx5_5BnwVz722FmSS5nxvL2HXJRnA00im5R4Ebo='
f = Fernet(key)

def encrypt(message):
    encoded = message.encode()
    encrypt = f.encrypt(encoded)
    return encrypt
def decrypt(e_message):
    decrypt = f.decrypt(e_message)
    decode = decrypt.decode()
    return decode


