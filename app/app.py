# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from joblib import load
import numpy as np


app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])

def hello_world():
    request_str = request.method
    if request_str == 'GET':
        return render_template('index.html')
    else:
        month = request.form['Month']
        day = request.form['Day']
        hour = request.form['Hour']
        minute = request.form['Minute']
        cloud_type = request.form['CT']
        dew_point = request.form['DP']
        solar_zenith_angle = request.form['SZA']
        fill_flag = request.form['FF']
        surface_albedo = request.form['SA']
        wind_speed = request.form['WS']
        precipitable_water = request.form['PW']
        wind_direction = request.form['WD']
        relative_humidity = request.form['RH']
        temperature = request.form['Temperature']
        pressure = request.form['Pressure']

        np_input = np.array([float(month), float(day), float(hour), float(minute), float(cloud_type), float(dew_point), float(solar_zenith_angle), float(fill_flag), float(surface_albedo), float(wind_speed), float(precipitable_water), float(wind_direction), float(relative_humidity), float(temperature), float(pressure)])

        model = load('app/model.joblib')

        pred = model.predict(np_input)

        return render_template('index.html', ans = str(predict_exact(pred))+' '+u'W/m\u00B2')

    
        
    
def predict_exact(pred):
    ans = 0
    if pred < 0:
        ans = 0
    else:
        ans= int(pred)
    return ans

    

