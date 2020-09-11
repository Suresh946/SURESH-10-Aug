# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:05:14 2020

@author: acer
"""

from flask import Flask,redirect, url_for, request
app= Flask(__name__)

@app.route('/sucess/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/login',method=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('success' ,name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success' ,name = user))
                          
if __name__ == '__main__':
    app.run(debugss=True)