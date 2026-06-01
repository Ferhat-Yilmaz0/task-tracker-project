import os

from app import create_app, db

config_name = os.environ.get("FLASK_ENV", "development")
app = create_app(config_name)

# Teslim sırasında migration sorununa takılmamak için SQLite tablolarını otomatik oluşturur.
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
