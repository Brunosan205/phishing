from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f'Username: {username}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)