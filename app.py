from flask import Flask
from app_regression.routes import regression_bp
from app_knn.routes import knn_bp

app = Flask(__name__)

# Crear y registrar los dos modulos en la aplcación, con diferentes prefijos de URL
app.register_blueprint(regression_bp, url_prefix='/regression')
app.register_blueprint(knn_bp, url_prefix='/knn')

if __name__ == '__main__':
    app.run(debug=True)