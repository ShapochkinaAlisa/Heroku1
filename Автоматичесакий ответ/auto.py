from flask import Flask, render_template
app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    p = {}
    p['title'] = 'Миссия будет хороша)'
    p['surname'] = 'Shapochkina'
    p['name'] = 'Alisa'
    p['education'] = 'Среднее'
    p['profession'] = 'программист'
    p['sex'] = 'girl'
    p['motivation'] = 'На Марс!'
    p['ready'] = 'Yes!'
    return render_template('auto_answer1.html', **p)

if __name__ == '__main__':
    app.run(port=7001, host='127.0.0.1')