from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(
        'Usuário',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Senha',
        validators=[DataRequired()]
    )
    confirmPassword = PasswordField(
        'Confirmar senha',
        validators=[DataRequired(),EqualTo('password')]
    )