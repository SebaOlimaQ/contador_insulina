from flask import Blueprint, redirect, render_template, request, url_for
from registro import RegistroForm
from inicio_sesion import TuFormularioDeInicioSesion

# Crear un Blueprint para las rutas relacionadas con el registro
registro_bp = Blueprint('registro', __name__)


@registro_bp.route('/registro')
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        # Procesar el formulario si se ha enviado y es válido
        return render_template('registro.html', form=form)
    return render_template('registro.html', form=form)


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


@main_bp.route('/')
def index():
    return render_template('index.html')
