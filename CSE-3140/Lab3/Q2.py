import os
import subprocess
import sys
  
def shafy(app): # runs sha256sum with a file and grabs the resulting hash value
  os.chdir('/home/cse/Lab3/Q2files')
  result = subprocess.run(['sha256sum', app], stdout=subprocess.PIPE)
  piece = result.stdout.split()
  return piece

def main():
  apps = [] # list of .exe files
  for file in os.listdir('/home/cse/Lab3/Q2files'):
    if file[-4:] == ".exe":
      apps.append(file)
  
  os.chdir('/home/cse/Lab3')
  result = subprocess.run(['cat', 'Q2hash.txt'], stdout=subprocess.PIPE)
  tester = result.stdout
  tester = tester[:-1] # this is the hash value to test all files against

  for i in apps:
    value, app = shafy(i)
    if value == tester:
      print('success: app with same hash value is', app)
    
main()