from flask import Flask

app = Flask(__name__)

@app.route('/users/hello')
def hello():
    return 'Hello, welcome to the ESBay User API\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)