from flask import Flask, render_template, request, send_file
import csv
import os 
import squarify

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

import io
import base64

style.use("ggplot")
sns.set_palette("bright")
from warnings import filterwarnings
filterwarnings("ignore")
import os
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_colwidth', None)

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')
@app.route('/')


@app.route('/upload', methods=['POST'])

def front(self, n):
    return self.iloc[:, :n]

def back(self, n):
    return self.iloc[:, -n:]

def connectedProducts():
    out = pd.read_csv("dataConnected.csv")
    top20items = pd.DataFrame(out["gtin"].value_counts().head(20))
    top20items = top20items.reset_index()
    top20items.columns = ["Itemname","Frequency"]
    labels = top20items["Itemname"]
    sizes = top20items["Frequency"]

    pd.DataFrame.front = front
    pd.DataFrame.back = back 

    fig = plt.figure(figsize=(25,6))
    colors = sns.color_palette("Spectral",20)
    squarify.plot(sizes, label=labels, color =  colors)
    plt.title("Top 20 Products")
    img = plt.savefig('connectedProducts.png')
    return plt

def weatherCorrelation():
    weather = pd.read_csv("data.csv")
    weather = weather.drop(columns = "Unnamed: 0")
    weather['dt'] =  pd.to_datetime(weather['dt'])
    weather = weather.set_index('dt')
    grouped = weather.groupby(['temp','gtin']).sum()
    grouped_cnt = grouped.drop(columns = "price")
    grouped_price = grouped.drop(columns = "cnt")
    pd.DataFrame.front = front
    pd.DataFrame.back = back
    fig, ax = plt.subplots(figsize=(30,15))
    grouped_cnt.unstack().front(50).plot(ax=ax)
    fig, ax = plt.subplots(figsize=(30,15))
    grouped_price.unstack().front(50).plot(ax=ax)
    img = plt.savefig('Weather.png')
    return img

def get_graph():
    plt = weatherCorrelation() 
    # Save the graph to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Return the graph as a binary response
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
