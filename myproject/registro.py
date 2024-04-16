from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class RegistroForm(FlaskForm):
    nombre_completo = StringField('Nombre Completo', [
                                  validators.Length(min=4, max=50), validators.DataRequired()])
    localidad = StringField('Localidad', [validators.Length(
        min=4, max=50), validators.DataRequired()])
    usuario = StringField('Usuario', [validators.Length(
        min=4, max=25), validators.DataRequired()])
    contraseña = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirmar_contraseña',
                           message='Las contraseñas deben coincidir'),
        validators.Length(min=6, max=25)
    ])
    confirmar_contraseña = PasswordField('Confirmar Contraseña')
