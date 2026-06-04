from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprint 등록 (URL 접두사 설정)
    from .routes import bp
    app.register_blueprint(bp)

    return app

app = create_app()
