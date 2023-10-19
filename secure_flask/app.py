from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'test!'


if __name__ == '__main__':
    app.run(
    port=4321,
    ssl_context=('localhost.pem', 'localhost-key.pem')
    )