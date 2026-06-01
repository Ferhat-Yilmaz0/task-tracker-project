from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    """Yeni kullanıcı kayıt formu."""

    username = StringField(
        "Kullanıcı Adı",
        validators=[DataRequired(), Length(min=3, max=64)],
    )
    email = StringField(
        "E-posta",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(
        "Şifre",
        validators=[DataRequired(), Length(min=6)],
    )
    password2 = PasswordField(
        "Şifreyi Onayla",
        validators=[DataRequired(), EqualTo("password", message="Şifreler eşleşmiyor.")],
    )
    submit = SubmitField("Kayıt Ol")

    def validate_username(self, field):
        """Kullanıcı adının daha önce alınmadığını doğrular."""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Bu kullanıcı adı zaten kullanılıyor.")

    def validate_email(self, field):
        """E-posta adresinin daha önce kayıtlı olmadığını doğrular."""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Bu e-posta adresi zaten kayıtlı.")


class LoginForm(FlaskForm):
    """Kullanıcı giriş formu."""

    email = StringField(
        "E-posta",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(
        "Şifre",
        validators=[DataRequired()],
    )
    remember_me = BooleanField("Beni Hatırla")
    submit = SubmitField("Giriş Yap")
