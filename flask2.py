# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:46:52 2020

@author: acer
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return ("Hello interns\n i think i done my project please give me inrernship certificate as soon as possible\n thank you")

if __name__ == '__main__':
    app.run()
    
           
    
           
           