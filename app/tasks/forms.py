from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    title = StringField(
        "Başlık",
        validators=[DataRequired(message="Başlık gerekli."), Length(max=128)],
    )
    description = TextAreaField("Açıklama", validators=[Length(max=1000)])
    submit = SubmitField("Görev Ekle")
