# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:18:28 2020

@author: a
"""

from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def get_value():
    name=request.form['search']
    print(name)
    return render_template('pass.html', n=name)

if __name__ == '__main__':
    app.run(debug=True)
