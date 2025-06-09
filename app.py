from flask import Flask
import logging
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)

# متریک Prometheus
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")

# تنظیمات لاگ
logging.basicConfig(filename="app.log", level=logging.INFO)

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    logging.info("Home page visited")
    return "Hello, World!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
