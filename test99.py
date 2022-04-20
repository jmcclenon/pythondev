from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Numbers Pro v0.1.0</h1>'

@app.route('/about')
def about_page():
    return '<h1>About Numbers Pro v0.1.0</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)