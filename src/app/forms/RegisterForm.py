from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import Email, Length, InputRequired, EqualTo, NumberRange


class RegisterForm(FlaskForm):
    first_name = StringField('Nombre', validators=[
        InputRequired(message="Debe ingresar un nombre valido"),
        Length(message="Su clave debe tener entre 5 y 16 caracteres", min=2, max=255)

    ], render_kw={'class': "form-control"})
    last_name = StringField('Apellido', validators=[
        InputRequired(message="Debe ingresar un nombre valido"),
        Length(message="Su clave debe tener entre 5 y 16 caracteres", min=2, max=255)

    ], render_kw={'class': "form-control"})
    email = StringField('Email', validators=[
        InputRequired(message="Debe ingresar un email valido"),
        Email(message="Debe ingresar un email válido"),
        Length(message="Su email debe tener mas de 5 cracteres", min=5)
    ], render_kw={'class': "form-control"})
    password = PasswordField('Password', validators=[
        InputRequired(message="Debe ingresar un email valido"),
        Length(message="Su clave debe tener entre 5 y 16 caracteres", min=5, max=16),
        EqualTo('confirm_password')
    ], render_kw={'class': "form-control"})
    confirm_password = PasswordField('Confirmar password', validators=[
        InputRequired(message="Debe ingresar un email valido"),
        Length(message="Su clave debe tener entre 5 y 16 caracteres", min=5, max=16)
    ], render_kw={'class': "form-control"})


class LenderRegisterForm(RegisterForm):
    money = IntegerField("Cantidad de dinero a necesitar (USD)", validators=[
        InputRequired(message="Este campo es necesario"),
        NumberRange(message="El monto debe ser mayor a 100 USD", min=100)
    ])


class BorrowerRegisterForm(RegisterForm):
    money = IntegerField("Cantidad de capital (USD)", validators=[
        InputRequired(message="Este campo es necesario"),
        NumberRange(message="El monto debe ser mayor a 100 USD", min=100)
    ])
    project_title = StringField('Nombre proyecto', validators=[
        InputRequired(message="Debe ingresar un nombre valido"),
        Length(message="Su nombre debe tener entre 2 y 255 caracteres", min=2, max=255)
    ], render_kw={'class': "form-control"})
    project_description = TextAreaField('Descripción Proyecto', validators=[
        InputRequired(message="Debe ingresar un nombre valido"),
        Length(message="Su descripción debe tener entre 2 y 1024 caracteres", min=2, max=1024)
    ], render_kw={'class': "form-control"})

