from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/sign up', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return f'Thanks for submitting the form {request.form["fname"]}!'
    return render_template("signup.html", signup=url_for('signup'))

@app.route('/goodbue')
def goodbye():
    return 'goodbye World'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug = True)