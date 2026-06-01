import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config_by_name

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = "auth.login"
login_manager.login_message = "Bu sayfayı görmek için giriş yapmalısınız."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id: str):
    from app.models import User

    try:
        return User.query.get(int(user_id))
    except (TypeError, ValueError):
        return None


def create_app(config_name: str = "default") -> Flask:
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    app.config.from_object(config_by_name[config_name])
    config_by_name[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Modeller migrate/create_all tarafından görülsün.
    from app import models  # noqa: F401

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.tasks import tasks as tasks_blueprint
    app.register_blueprint(tasks_blueprint, url_prefix="/tasks")

    return app
