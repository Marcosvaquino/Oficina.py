from flask import Blueprint, redirect,render_template,request,url_for
from Model.carro import Carro
from Controller.carroBLL import *

carro = Blueprint('carro',__name__,template_folder="View")

@carro.route('/carro')
def index_carro():
    return render_template('carro.html',carros = CarroBLL.getListCarros())

@carro.route('/carro/cadastrar', methods=['POST'])
def cadastrar():

    novo_carro = Carro()

    novo_carro.id_oficina = 1
    novo_carro.id_cliente = request.form['id cliente']
    novo_carro.placa = request.form['placa']
    novo_carro.modelo = request.form['modelo']
    novo_carro.marca = request.form['marca']
    novo_carro.cor = request.form['cor']
    novo_carro.cor = request.form['ano fabricacao']
    novo_carro.cor = request.form['ano modelo']


    CarroBLL.setCarro(novo_carro)

    return redirect(url_for('carro.index_carro'))

@carro.route('/carro/consultar/<placa>')
def consultar(placa):
    carro = CarroBLL.getCarro(placa)

    return render_template('consulta.html')