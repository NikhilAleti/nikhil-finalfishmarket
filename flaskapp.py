# -*- coding: utf-8 -*-
"""Flaskapp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UEyS8OvRmokJGFrDb5JU9RCLLRcQ1ga1
"""

import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    
    return render_template('index.html', prediction_text='The species of the fish is {}'.format(prediction))
    
    


if __name__=='__main__':
    app.run()