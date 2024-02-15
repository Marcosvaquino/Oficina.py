from flask import Blueprint, redirect,render_template,request, session,url_for
from Model.carro import Carro
from Controller.carroBLL import *

carro = Blueprint('carro',__name__,template_folder="View")

@carro.route('/carro')
def index_carro():
    return render_template('Carros/carro.html',carros = CarroBLL.getListCarros(),pagina='Carros')

@carro.route('/carro/cadastrar', methods=['POST'])
def cadastrar():

    novo_carro = Carro()

    novo_carro.id = request.form['id']
    novo_carro.id_oficina = session['id_oficina']
    novo_carro.id_cliente = request.form['id_cliente']
    novo_carro.placa = request.form['placa']
    novo_carro.modelo = request.form['modelo']
    novo_carro.marca = request.form['marca']
    novo_carro.cor = request.form['cor']
    novo_carro.ano_fabricacao = request.form['ano_fabricacao']
    novo_carro.ano_modelo = request.form['ano_modelo']

    if novo_carro.id == 0:
        CarroBLL.setCarro(novo_carro)
    else:
        CarroBLL.updateCarro(novo_carro)

    return redirect(url_for('carro.index_carro'))

@carro.route('/carro/consultar/<placa>')
def consultar(placa):
    carro = CarroBLL.getCarro(placa)

    return render_template('consulta.html')