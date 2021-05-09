from cryptography.fernet import Fernet
from encrypt import genwrite_key, get_key
password = input("enter password for: ")
Enc_password = password.encode()
key = get_key()
a = Fernet(key)
encrypt_password = a.encrypt(Enc_password)
print(encrypt_password)
