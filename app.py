from flask import Flask
from routes import avatarRoutes


app = Flask(__name__)
app.register_blueprint(avatarRoutes.bp)

@app.route('/')
def index():
    return "Hello Worldzzz"

if __name__ == '__main__':
    app.run()
