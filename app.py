# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:40:42 2023

@author: AFOMIKE
"""

import flask
import pickle
import pandas as pd

laptop_list = pd.read_csv('model/laptop_list.csv')
with open(f'model/laptopsimilarity.pkl', 'rb') as f:
    laptop_similarity = pickle.load(f)



phone_list = pd.read_csv('model/phone_list.csv')
with open(f'model/phonesimilarity.pkl', 'rb') as f:
    phone_similarity = pickle.load(f)

def recommendlaptop(laptop,os_brand):
    index = laptop_list[(laptop_list['usecases']==laptop) & (laptop_list['os_brand']==os_brand)].index[0]
    distances = sorted(list(enumerate(laptop_similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    printed_names = set()

    for i in distances[1:8]:
        row_index = i[0]
        name = laptop_list.iloc[row_index]['name']
        if name not in printed_names:
            printed_names.add(name)
            recommended_names.append(name)

    return recommended_names

def recommendphone(Name):
    index = phone_list[phone_list['Name'] == Name].index[0]
    distances = sorted(list(enumerate(phone_similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    printed_names = set()

    for i in distances[1:8]:
        row_index = i[0]
        name = phone_list.iloc[row_index]['Name']
        if name not in printed_names:
            printed_names.add(name) 
            recommended_names.append(name)

    return recommended_names

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        device = flask.request.form.get("selectedDevice")
        OpS = flask.request.form.get("selectedOS")
        Job = flask.request.form.get("selectedJob")
        Budget = flask.request.form.get("selectedBudget")    
        if device == 'Phone'  and Job == " Business/Professional":
           recommendphone('Realme Narzo 20 Pro (White Knight, 64 GB)')
           prediction = recommendphone('Realme Narzo 20 Pro (White Knight, 64 GB)')
        elif device =='Laptop':
           prediction =recommendlaptop(Job,OpS)
        elif device == 'Phone'  and Job == " Gaming":
          prediction = recommendphone('POCO M2 (Pitch Black, 64 GB)')
        elif device == 'Phone'  and Job == " Multimedia/Entertainment":
          prediction = recommendphone('Samsung Galaxy M30s (Black, 128 GB))')
        elif device == 'Phone'  and Job == " Budget Friendly":
          prediction = recommendphone('Lenovo Z6 Pro (Black, 128 GB)')
        elif  device == 'Phone'  and Job ==" Home/Everyday use":
          prediction = recommendphone('OPPO Reno3 Pro (Sky White, 128 GB)')
        elif  device == 'Phone'  and Job ==" Creative/Design":
           prediction = recommendphone('Redmi Note 8 Pro (Halo White, 64 GB)')
        else:
           prediction = recommendphone('POCO X2 (Matrix Purple, 64 GB)')
        response = {
        "result": prediction
        }

        return flask.jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
