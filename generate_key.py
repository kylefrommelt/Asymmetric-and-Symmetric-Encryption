from cryptography.fernet import Fernet

first_key = Fernet.generate_key()

file = open('key.txt', 'wb')
file.write(first_key)
file.close()
