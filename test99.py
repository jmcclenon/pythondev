from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'John... Hello World! This is your world'
    
if __name__ == '__main__':
    app.run(debug=True)