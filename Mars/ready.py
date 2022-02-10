from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = "Миссия Колонизация Марса"
    ttt = "И на Марсе будут яблони цвести!"
    return render_template('base.html', title='Заготовка',
                           username=user, text=ttt)


if __name__ == '__main__':
    app.run(port=8022, host='127.0.0.1')
