import os

from app import auth_app
from flask_jwt_extended import JWTManager

config_name = os.getenv('APP_SETTINGS')
app = auth_app(config_name)


if __name__ == "__main__":
    app.run(debug=True)
