from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

salt = get_random_bytes(16)  
password = '37s8x98xzxcv9201'
key = PBKDF2(password, salt, dkLen=32)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
command = 'print("hello")'
padded_command = pad(command.encode(), AES.block_size)
ciphered_data = cipher.encrypt(padded_command)

print(f"Ciphered data: {ciphered_data}")











