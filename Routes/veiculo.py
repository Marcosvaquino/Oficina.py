from flask import Blueprint, redirect,render_template,request, session,url_for
from Model.veiculo import Veiculo
from Controller.veiculoBLL import *

veiculo = Blueprint('veiculo',__name__,template_folder="View")

@veiculo.route('/veiculo')
def index_veiculo():
    return render_template('Veiculos/veiculo.html',veiculos = VeiculoBLL.getListVeiculos(),pagina='Veiculos')

@veiculo.route('/veiculo/cadastrar', methods=['POST'])
def cadastrar():

    novo_veiculo = Veiculo()

    novo_veiculo.id = request.form['id']
    novo_veiculo.id_oficina = session['id_oficina']
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

@veiculo.route('/veiculo/consultar/<placa>')
def consultar(placa):
    veiculo = VeiculoBLL.getVeiculo(placa)

    return render_template('consulta.html')