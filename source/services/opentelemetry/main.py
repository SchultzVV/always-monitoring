from flask import Flask
import os

# Importa e ativa as métricas
from app import metrics  # Isso ativa o MeterProvider e começa a exportar

app = Flask(__name__)

@app.route("/")
def index():
    return "🔍 Observability service is running with local metrics!"

if __name__ == "__main__":
    app.run(
        debug=os.getenv("LOG", "False") == "True",
        host="0.0.0.0",
        port=5000
    )
