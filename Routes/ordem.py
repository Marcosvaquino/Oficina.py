from flask import Blueprint, redirect,render_template,request, session,url_for
from Model.veiculo import Veiculo
from Model.ordem_servico import os
from Controller.veiculoBLL import *

ordem = Blueprint('ordem',__name__,template_folder="View")

@ordem.route('/ordem')
def index_veiculo():

    ordem= os()
    ordem.id = 0
    ordem.id_cliente = 0
    ordem.id_veiculo = 0
    ordem.id_oficina = 0
    ordem.data_criacao= ''
    ordem.data_atualizacao = ''
    ordem.status = 1


    return render_template('Ordens/os.html',pagina='Ordem de Serviço',os=ordem)

@ordem.route('/ordem/cadastrar', methods=['POST'])
def cadastrar():

    novo_veiculo = Veiculo()

    novo_veiculo.id = request.form['id']
    novo_veiculo.id_oficina = session['id_oficina']
    novo_veiculo.id_cliente = request.form['id_cliente']
    novo_veiculo.placa = request.form['placa']
    novo_veiculo.modelo = request.form['modelo']
    novo_veiculo.marca = request.form['marca']
    novo_veiculo.cor = request.form['cor']
    novo_veiculo.ano_fabricacao = request.form['ano_fabricacao']
    novo_veiculo.ano_modelo = request.form['ano_modelo']

    if novo_veiculo.id == 0:
        VeiculoBLL.setVeiculo(novo_veiculo)
    else:
        VeiculoBLL.updateVeiculo(novo_veiculo)

    return redirect(url_for('veiculo.index_veiculo'))

@ordem.route('/ordem/consulta')
def consultar(placa):
    veiculo = VeiculoBLL.getVeiculo(placa)

    return render_template('consulta.html')