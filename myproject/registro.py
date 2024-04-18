from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, NumberRange


class RegistroForm(FlaskForm):
    nombre_completo = StringField('Nombre Completo', [
                                  validators.Length(min=4, max=50), validators.DataRequired()])
    ratio_1 = DecimalField('Ratio Bloque 1', validators=[
                           DataRequired(), NumberRange(min=0.1)])
    ratio_2 = DecimalField('Ratio Bloque 2', validators=[NumberRange(min=0.1)])
    ratio_3 = DecimalField('Ratio Bloque 3', validators=[NumberRange(min=0.1)])
    ratio_4 = DecimalField('Ratio Bloque 4', validators=[NumberRange(min=0.1)])
    submit = SubmitField('Guardar')
    usuario = StringField('Usuario', [validators.Length(
        min=4, max=25), validators.DataRequired()])
    contraseña = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirmar_contraseña',
                           message='Las contraseñas deben coincidir'),
        validators.Length(min=6, max=25)
    ])
    confirmar_contraseña = PasswordField('Confirmar Contraseña')
