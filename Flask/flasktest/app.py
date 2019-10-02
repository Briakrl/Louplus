#!/usr/bin/env python3

from flask import Flask
from flask import url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Shiyanlou!'

@app.route('/courses/<name>')
def course(name):
    return render_template('courses.html', coursename=name)

@app.route('/test')
def test():
    print(url_for('course', name='java', _external=True))
    return redirect(url_for('index'))

@app.route('/httptest')
def httptest():
    if request.method == 'GET':
        print(request.args.get('t'))
        print(request.args.get('q'))
        return 'It is a get request!'
    if request.method == 'POST':
        print(request.form.getlist('Q'))
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()
