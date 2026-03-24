''' removes encrypted files and populates victims folder with victim files for testing '''

import os

for anything in os.scandir('/home/cse/Lab3/Q6files/Victims'):
  os.remove(anything.path)

with open('/home/cse/Lab3/Q6files/Victims/v1.txt', 'w') as f:
  f.write('hello i am a hapless victim')
  
with open('/home/cse/Lab3/Q6files/Victims/v2.txt', 'w') as f:
  f.write('this directory is definitely very safe')
  
with open('/home/cse/Lab3/Q6files/Victims/v3.txt', 'w') as f:
  f.write('wow no way anyone\'s holding me for ransome')
  
with open('/home/cse/Lab3/Q6files/Victims/v4.txt', 'w') as f:
  f.write('imagine being hacked lol couldn\'t be me')
  
with open('/home/cse/Lab3/Q6files/Victims/v5.txt', 'w') as f:
  f.write('i\'m so hungry')

try:
  os.remove('/home/cse/Lab3/Q6files/EncryptedSharedKey.txt')
except:
  x = 1
  
print('success: directory reset')