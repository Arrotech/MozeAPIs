import os

from app import exam_app
from app.api.v1.models.database import Database

config_name = os.getenv('APP_SETTINGS')
app = exam_app(config_name)


@app.cli.command()
def create():
    """Create tables."""

    Database().create_table()


@app.cli.command()
def admin():
    Database().create_admin()

@app.cli.command()
def bursar():
    Database().create_bursar()

@app.cli.command()
def destroy():
    """Destroy tables."""

    Database().destroy_table()


if __name__ == '__main__':
    app.run(debug=True)
