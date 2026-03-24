import os
import sys
import Crypto
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

keyString = open('/home/cse/Lab3/Q3pk.pem').read()
key = RSA.importKey(keyString) # creates key
t = Crypto.Signature.PKCS1_v1_5.new(key) # key to test against all signatures in Q3files

for f in os.scandir('/home/cse/Lab3/Q3files'):
  if f.path.endswith('.sign'):
    app = f.path.rstrip('.sign') # file path to the executable file
    sig = f.path # file path to the signature
    
    with open(app, 'rb') as f: data = f.read() # reads content of the executable file
    h = SHA256.new(data) # creates hash
    with open(sig, 'rb') as f: signature = f.read() # reads signature of the file
    
    if t.verify(h, signature):
      print(f'success: {app}') # prints file if the file is correctly signed