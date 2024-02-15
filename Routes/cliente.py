from flask import Blueprint, redirect,render_template,request, session,url_for
from Model.cliente import Cliente
from Controller.clienteBLL import ClienteBLL
from Controller.form import CadastroCliente

cliente = Blueprint('cliente',__name__,template_folder="View")

@cliente.route('/cliente')
def index_cliente():
    form = CadastroCliente()
    return render_template('Clientes/cliente.html',clientes = ClienteBLL.getListClientes(),form = form,pagina='Clientes')

@cliente.route('/cliente/cadastrar', methods=['POST'])
def cadastrar():

    novo_cliente = Cliente()

    novo_cliente.id = request.form['id']
    novo_cliente.id_oficina = session['id_oficina']
    novo_cliente.nome = request.form['nome']
    novo_cliente.cpf_cnpj = request.form['cpf_cnpj']
    novo_cliente.fone = request.form['fone']
    novo_cliente.logradouro = request.form['logradouro']
    novo_cliente.cep= request.form['cep']
    novo_cliente.numero = request.form['numero']
    novo_cliente.bairro = request.form['bairro']
    novo_cliente.cidade = request.form['cidade']
    novo_cliente.uf= request.form['uf']
    novo_cliente.observacao = request.form['observacao']

    if novo_cliente.id == 0:
        ClienteBLL.setCliente(novo_cliente)
    else:
        ClienteBLL.updateCliente(novo_cliente)
   
    return redirect(url_for('cliente.index_cliente'))

