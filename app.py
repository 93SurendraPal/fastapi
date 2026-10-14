from flask import Flask
#from routes.incidents import incident_bp
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

#app.register_blueprint(incident_bp)

@app.route("/health")
def health():
    return {"status":"UP"}
@app.route("/surendra"):
    return {"status":"success","message":"Hello I am surendra Pal"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
