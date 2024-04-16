from flask import Flask
from routes import registro_bp, inicio_sesion_bp, main_bp

app = Flask(__name__)

# Registrar los Blueprints en la aplicación Flask
app.register_blueprint(registro_bp)
app.register_blueprint(inicio_sesion_bp)
app.register_blueprint(main_bp)
app.secret_key = 'your_secret_key'
if __name__ == '__main__':
    app.run(debug=True)
