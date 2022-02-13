from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/training/<job>')
def training(job):
    return render_template('training.html', job=job)


if __name__ == '__main__':
    app.run(port=8020, host='127.0.0.1')
