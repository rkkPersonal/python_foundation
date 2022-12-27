import requests
from flask import app, jsonify, Flask, request
from flask_sqlalchemy import SQLAlchemy
from paginator import Paginator
from sqlalchemy import create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
db = SQLAlchemy()

Base = declarative_base()

engine = create_engine('mysql://root:12345678@192.168.43.200:3306/python_db?charset=utf8')

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query_user_info(account):
    result = session.query(User, Role).filter(or_(User.account == account, account is None)).outerjoin(User.roles).limit(1).offset(0).all()

    print(result)
    lst = []
    for x in result:
        d = to_dict(x[0])
        print(d)
        print()
        if not x[1] is None:
            d['role'] = to_dict(x[1])
        lst.append(d)

    return lst


def to_dict(obj):
    from sqlalchemy import inspect
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs if c.key != 'nick_name'
            }


class User(db.Model):
    account = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(12))
    nick_name = db.Column(db.String(20))
    roles = db.relationship('Role', secondary='role_binding', back_populates='users')


class Role(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    users = db.relationship('User', secondary='role_binding', back_populates='roles')


class RoleBinding(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    user_id = db.Column(db.String(30), db.ForeignKey('user.account'), nullable=False)


@app.route('/user', methods=['GET'])
def customizeValue():
    keyword = request.args.get("keyword")
    data = query_user_info(keyword)
    return jsonify(data)


# if __name__ == '__main__':
#     query_user_info(None)

if __name__ == '__main__':
    app.debug = True
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=5000)
