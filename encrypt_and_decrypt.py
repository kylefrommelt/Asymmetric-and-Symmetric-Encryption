from generate_key import first_key
from cryptography.fernet import Fernet
  
key = Fernet(first_key)

# encrypt
with open('file.txt', 'rb') as file:
    key_file = file.read()
      

encrypted = key.encrypt(key_file)
  

with open('encrypted_file.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# decrypt

with open('encrypted_file.txt', 'rb') as encrypted_file2:
    encrypted = encrypted_file2.read()
  

decrypted = key.decrypt(encrypted)
  

with open('decrypted_file.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
