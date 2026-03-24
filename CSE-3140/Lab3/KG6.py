import os
import sys
import Crypto
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

priv = Crypto.PublicKey.RSA.generate(1024) # generates key pair
privKey = priv.exportKey() # creates key object to be stored

pub = priv.publickey() # generates public key based on private key generated
pubKey = pub.exportKey() # creates key object to be stored

with open('/home/cse/Lab3/Q6files/Solutions/e.key', 'wb') as f: f.write(pubKey)
with open('/home/cse/Lab3/Q6files/Solutions/d.key', 'wb') as f: f.write(privKey)