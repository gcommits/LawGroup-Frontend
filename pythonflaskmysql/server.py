from flask import Flask, render_template, request, redirect, session
from mydb import Email

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', method="POST")
def submit():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['phone'] = request.form['phone']
    session['subject'] = request.form['subject']
    session['message'] = request.form['message']
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'subject': request.form['subject'],
        'message': request.form['message']
    }
    return redirect('#')

@app.route('/subscribe', method="POST")
def subscribe():
    session['email'] = request.form['email']
    data = {
        'email': request.form['email']
    }
    Email.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)