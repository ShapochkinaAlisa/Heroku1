from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    app.run()


@app.route("/")
def index():
    print("b")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    print(names)
    return render_template("index.html", jobs=jobs, users=names)


if __name__ == '__main__':
    main()

