from flask import redirect, url_for
from flask_login import current_user

from app.main import main


@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("tasks.list_tasks"))
    return redirect(url_for("auth.login"))
