from flask import Flask
from routes import avatarRoutes

app = Flask(__name__)
app.register_blueprint(avatarRoutes.bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Starting Avatar Creation...'


if __name__ == '__main__':
    app.run()
