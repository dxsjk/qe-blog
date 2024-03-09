from utils.pwd import set_password
from sqlalchemy import inspect
from routes import app, db


def init_db():
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('users'):
            from models.user import User
            db.create_all()
            password_hashed = set_password('123456')
            user = User(username="root", password=password_hashed.decode('utf-8'), fullname='root', description='')
            db.session.add(user)
            db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
