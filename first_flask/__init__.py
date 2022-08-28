from flask import Flask

def create_app():
    app=Flask(__name__)

    from first_flask.user.view import mod as user_module

    app.register_blueprint(user_module)

    return app