from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class Login( FlaskForm ):
    usuario = StringField( 'Usuario', validators=[DataRequired( message='No dejar vacío, completar' )] )
    contrasena = StringField( 'Contraseña', validators=[DataRequired( message='No dejar vacío, completar' )] )
    login = SubmitField( 'Login' )
