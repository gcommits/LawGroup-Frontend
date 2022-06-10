from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['phone'] = request.form['phone']
    session['subject'] = request.form['subject']
    session['message'] = request.form['message']
    return redirect('#')

@app.route('/subscribe')
def subscribe():
    session['email'] = request.form['email']
    return redirect('#')

if __name__ == "__main__":
    app.run(debug=True)