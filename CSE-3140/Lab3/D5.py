from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util.Padding import unpad

hash_new = MD5.new()

with open("/home/cse/Lab3/Q5files/R5.py", "rb") as f:
  x = f.read()
  hash_new.update(x)

newf = hash_new.digest()

with open("/home/cse/Lab3/Q5files/Encrypted5", "rb") as file_2:
  iv = file_2.read(16)
  encoded = file_2.read()

cipher = AES.new(newf, AES.MODE_CBC, iv)
msg_decrypt = unpad(cipher.decrypt(encoded), AES.block_size)

print(msg_decrypt.decode())