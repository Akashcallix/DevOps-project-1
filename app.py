from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/personal-info')
def personal_info():
    return render_template('personal_info.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
