from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os

# Ativa o código de métricas
from app import metrics

app = Flask(__name__)

# Endpoint padrão da aplicação
@app.route("/")
def home():
    return "📡 Prometheus metric endpoint running!"

# Monta o app do Prometheus na rota /metrics
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})

if __name__ == "__main__":
    app.run(
        debug=os.getenv("LOG", "False") == "True",
        host="0.0.0.0",
        port=5000
    )
