import os
import sys

from flask import Flask, redirect,render_template,request,url_for
from Model.carro import Carro
from Controller.carroBLL import *

app = Flask(__name__,template_folder="View")

@app.route('/')
def index():
    return render_template('index.html',carros = listadeCarros)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():    
    placa = request.form['placa']
    modelo = request.form['modelo']
    marca = request.form['marca']
    cor = request.form['cor']

    novo_carro = Carro(1,placa,modelo,marca,cor)

    CarroBLL.setCarro(novo_carro)

    return redirect(url_for('index'))

@app.route('/consultar/<placa>')
def consultar(placa):
    carro = CarroBLL.getCarro(placa)

    return render_template('consulta.html')

app.run(debug=True)
