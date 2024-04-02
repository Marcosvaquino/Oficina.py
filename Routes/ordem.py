from flask import Blueprint, redirect,render_template,request, session,url_for
from Model.carro import Carro
from Model.ordem_servico import os
from Controller.carroBLL import *

ordem = Blueprint('ordem',__name__,template_folder="View")

@ordem.route('/ordem')
def index_carro():

    ordem= os()
    ordem.id = 0
    ordem.id_cliente = 0
    ordem.id_carro = 0
    ordem.id_oficina = 0
    ordem.data_criacao= ''
    ordem.data_atualizacao = ''
    ordem.status = 1


    return render_template('Ordens/os.html',pagina='Ordem de Serviço',os=ordem)

@ordem.route('/ordem/cadastrar', methods=['POST'])
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

@ordem.route('/ordem/consulta')
def consultar(placa):
    carro = CarroBLL.getCarro(placa)

    return render_template('consulta.html')