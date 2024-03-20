# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:15:49 2023

@author: AFOMIKE
"""

import pickle
import pandas as pd


# with open(f"model/laptop_list.pkl", "rb") as f:
#     laptop_list = pickle.load(f)
# laptop_list = pickle.load(open('model/laptop_list.pkl', 'rb'))
laptop_list = pd.read_csv('model/laptop_list.csv')
laptop_list= laptop_list.head()
with open(f'model/laptopsimilarity.pkl', 'rb') as f:
    laptop_similarity = pickle.load(f)
laptop_list.head()
index = laptop_list[laptop_list['name'] == 'Lenovo Intel Core i5 11th Gen']
index.index[0]

print(index)


def recommendlaptop(Name):
    index = laptop_list[laptop_list['name'] == Name].index[0]
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

recommendlaptop(" Gaming")