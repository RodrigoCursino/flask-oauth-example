from crypt import methods
from flask import Flask, request
from auth_middleware import token_required
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HELLO_WORLD'
@app.route("/")
@token_required
def hello_world(current_user):
    return "<p>Hello, World!</p>"


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        ### validar usuario
        # exemplo: https://www.loginradius.com/blog/engineering/guest-post/securing-flask-api-with-jwt/
        token  = jwt.encode(
                    {"racf":"teste"},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
        )
        return {
            "message": "Successfully fetched auth token",
            "data": token
        }

    except Exception as e:
        return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
        }, 500
