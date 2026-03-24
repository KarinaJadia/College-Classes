import time
import subprocess

# directory: /home/cse/Lab1/Q4/

f = open("/home/cse/Lab1/Q4/PwnedPWfile")
with open("/home/cse/Lab1/Q4/PwnedPWfile") as f:
  lines = [line.rstrip('\n') for line in f]
f.close()

start = time.time()
print(f'start time: {start - start}')

for l,i in enumerate(lines):
  x = i.split(',')
  user = x[0]
  pwd = x[1]
  print(f'Now testing {user}, user {l+1}/{len(lines)}')
  result = subprocess.run(["python3", "Login.pyc", user, pwd], capture_output = True, text = True, cwd = "/home/cse/Lab1/Q4/")
  if result.stdout == "Login successful.\n":
    print(result.stdout)
    print(f'\nusername: {user}\npassword: {pwd}')
    print(f'time taken: {time.time() - start:.2f}s')
    break