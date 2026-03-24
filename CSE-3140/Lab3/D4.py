from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

et = open('/home/cse/Lab3/Q4files/Encrypted4', 'rb')
bytes = et.read(16) # bytes of the encrypted text in hexadecimal
text = et.read() # the encrypted text
et.close()

key = open('/home/cse/Lab3/Q4files/.key.txt', 'rb').read() # reads the key

content = unpad(AES.new(key, AES.MODE_CBC, iv = bytes).decrypt(text), AES.block_size) # decryptes it
print('content:',content)