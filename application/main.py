from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registerpage')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)