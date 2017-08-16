from flask import Flask
import config
app = Flask(__name__)

app.config.update(
    DEBUG=config.DEBUG,
    SECRET_KEY=config.SECRET_KEY)


@app.route('/')
def hello_world():
    return 'Hello, World!'
