from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nextpage')
def nextpage():
    return render_template('nextpage.html')

@app.route('/thirdpage')
def bananer():
    return render_template('bananer.html')

if __name__ == '__main__':
    app.run(debug=True)