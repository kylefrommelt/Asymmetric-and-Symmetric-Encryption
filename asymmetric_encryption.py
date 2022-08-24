import rsa


message = 'secret message'
public_key, private_key = rsa.newkeys(512)
public_string = str(public_key)
private_string = str(private_key)


with open('rsa_sym_key_plain.txt', 'w') as rsa_sym_key_plain:
	rsa_sym_key_plain.write(public_string)
	rsa_sym_key_plain.write('\n')
	rsa_sym_key_plain.write(private_string)

encrypt = rsa.encrypt(message.encode(),
                         public_key)
encrypted_string = str(encrypt)

with open('rsa_encrypted_message.txt', 'w') as rsa_encrypted_message:
	rsa_encrypted_message.write(encrypted_string)


decrypt = rsa.decrypt(encrypt, private_key).decode()
decrypted_string = str(decrypt)

with open('rsa_decrypted_message.txt', 'w') as rsa_decrypted_message:
	rsa_decrypted_message.write(decrypted_string)
