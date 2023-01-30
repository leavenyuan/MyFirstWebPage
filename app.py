# -*- coding: utf-8 -*-
# @Time    : 2023/1/16 8:03 PM
# @Author  : Yuan Xiaolu
# @Email   : yuanxiaolu@sensetime.com
# @File    : app.py
# @ Describe: 
# @ Reference:

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
app = Flask(__name__)
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app


@app.route('/hello')
def hello():
    # return 'Welcome to My Watchlist!'
    # return '<ion-icon name="accessibility-outline"></ion-icon>'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
