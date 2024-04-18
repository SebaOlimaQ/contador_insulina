from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
import pytz
from registro import RegistroForm
from inicio_sesion import TuFormularioDeInicioSesion
from contador import CalculadoraInsulina

# Crear un Blueprint para las rutas relacionadas con el registro
registro_bp = Blueprint('registro', __name__)


@registro_bp.route('/registro')
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        # Procesar el formulario si se ha enviado y es válido
        ratio_1 = form.ratio_1.data
        ratio_2 = form.ratio_2.data
        ratio_3 = form.ratio_3.data
        ratio_4 = form.ratio_4.data

        return redirect(url_for('registro.exito'))
    return render_template('registro.html', form=form)


@registro_bp.route('/exito')
def exito():
    return "¡Registro exitoso!"


# Crear un Blueprint para las rutas relacionadas con el inicio de sesión
inicio_sesion_bp = Blueprint('inicio_sesion', __name__)


@inicio_sesion_bp.route('/inicio_sesion')
def inicio_sesion():
    form = TuFormularioDeInicioSesion()
    if request.method == 'POST' and form.validate():
        # Lógica para manejar el inicio de sesión aquí
        # Redirige a alguna página después de iniciar sesión
        return redirect(url_for('index'))
    return render_template('inicio_sesion.html', form=form)


# Crear un Blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

calculadora = CalculadoraInsulina()


historial = []  # Lista para almacenar el historial de consultas


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    global historial  # Usamos 'global' para acceder a la lista 'historial'

    if request.method == 'POST':
        if 'carbs' in request.form and 'ratio' in request.form:
            carbohidratos_consumidos = float(request.form['carbs'])
            ratio = int(request.form['ratio'])
            cantidad_insulina = calculadora.calcular_insulina(
                carbohidratos_consumidos, ratio)

            # Agregamos la información de la consulta al historial
            historial.append({
                'carbs': carbohidratos_consumidos,
                'ratio': ratio,
                'hora': datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime('%H:%M'),
                'insulina_sugerida': cantidad_insulina
            })

            return render_template('index.html', insulina=cantidad_insulina, ratio=ratio, carbohidratos_consumidos=carbohidratos_consumidos, historial=historial)
        else:
            hora_actual = datetime.now(pytz.timezone(
                'America/Argentina/Buenos_Aires')).strftime('%H:%M')

            return render_template('index.html', hora_actual=hora_actual, historial=historial)
    else:
        hora_actual = datetime.now(pytz.timezone(
            'America/Argentina/Buenos_Aires')).strftime('%H:%M')

        return render_template('index.html', hora_actual=hora_actual, historial=historial)
