from flask import Flask, render_template, redirect, url_for, request, jsonify
import RPi.GPIO as GPIO
import time



app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            print("triggered from web")


        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/google', methods = ['POST'])
def switch():
    cont = request.get_json()
    global BlindState
    if cont is not None:
        print("got request from google Opening")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(31, True)
        GPIO.output(37, True)
        GPIO.output(15, True)
        time.sleep(14)
        GPIO.output(15, False)
        GPIO.output(31, False)
        GPIO.output(37, False)

    return jsonify({"SUCCESS":True})

@app.route('/googleClose', methods = ['POST'])
def switch2():
    cont = request.get_json()
    global BlindState
    if cont is not None:
        print("got request from google Closing")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, True)
        time.sleep(21)
        GPIO.output(15, False)
    return jsonify({"SUCCESS":True})

@app.route('/state', methods = ['GET','POST'])
def showState():
    global BlindState
    return render_template('state.html', BlindState = BlindState)  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host = '0.0.0.0')
