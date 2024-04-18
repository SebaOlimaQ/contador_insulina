from flask import Flask


# from routes import app


app = Flask(__name__)


class CalculadoraInsulina:
    def __init__(self):
        self.gr_por_ui_por_horas = {}

    def calcular_insulina(self, carbohidratos_consumidos, ratio):
        insulina = carbohidratos_consumidos * 1 / ratio
        return insulina


# calculadora = CalculadoraInsulina()


# @app.route('/', methods=['GET', 'POST'])
# def index():
    # if request.method == 'POST':
        # if 'carbs' in request.form and 'ratio' in request.form:
        # carbohidratos_consumidos = float(request.form['carbs'])
        # ratio = int(request.form['ratio'])
        # cantidad_insulina = calculadora.calcular_insulina(
        # carbohidratos_consumidos, ratio)
        # return render_template('index.html', insulina=cantidad_insulina, ratio=ratio, carbohidratos_consumidos=carbohidratos_consumidos)
    # else:
        # hora_actual = datetime.now(pytz.timezone(
        #  'America/Argentina/Buenos_Aires')).strftime('%H:%M')
        # return render_template('index.html', hora_actual=hora_actual)


if __name__ == '__main__':
    app.run(debug=True)
