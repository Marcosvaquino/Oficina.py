from flask import Blueprint, redirect,render_template,request,url_for
from Model.carro import Carro
from Controller.carroBLL import *

carro = Blueprint('carro',__name__,template_folder="View")

@carro.route('/carro')
def index_carro():
    return render_template('carro.html',carros = listadeCarros)

@carro.route('/carro/cadastrar', methods=['POST'])
def cadastrar():    
    placa = request.form['placa']
    modelo = request.form['modelo']
    marca = request.form['marca']
    cor = request.form['cor']

    novo_carro = Carro(1,placa,modelo,marca,cor)

    CarroBLL.setCarro(novo_carro)

    return redirect(url_for('carro.index_carro'))

@carro.route('/carro/consultar/<placa>')
def consultar(placa):
    carro = CarroBLL.getCarro(placa)

    return render_template('consulta.html')