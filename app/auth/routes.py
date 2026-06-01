from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.models import User
from app.auth import auth
from app.auth.forms import RegisterForm, LoginForm


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Yeni kullanıcı kayıt rotası."""
    if current_user.is_authenticated:
        return redirect(url_for("tasks.list_tasks"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Hesabınız başarıyla oluşturuldu. Hoş geldiniz!", "success")
        return redirect(url_for("tasks.list_tasks"))

    return render_template("auth/register.html", title="Kayıt Ol", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Kullanıcı giriş rotası."""
    if current_user.is_authenticated:
        return redirect(url_for("tasks.list_tasks"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Geçersiz e-posta veya şifre.", "danger")
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember_me.data)
        flash(f"Hoş geldiniz, {user.username}!", "success")

        # Güvenli next parametresi yönlendirmesi
        next_page = request.args.get("next")
        if not next_page or not next_page.startswith("/"):
            next_page = url_for("tasks.list_tasks")
        return redirect(next_page)

    return render_template("auth/login.html", title="Giriş Yap", form=form)


@auth.route("/logout")
@login_required
def logout():
    """Kullanıcı çıkış rotası."""
    logout_user()
    flash("Başarıyla çıkış yaptınız.", "info")
    return redirect(url_for("tasks.list_tasks"))
