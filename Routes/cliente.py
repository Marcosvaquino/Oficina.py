from flask import Blueprint, redirect,render_template,request,url_for
from Model.cliente import Cliente
from Controller.clienteBLL import ClienteBLL

cliente = Blueprint('cliente',__name__,template_folder="View")

@cliente.route('/cliente')
def index_cliente():
    return render_template('pre_cadastro.html',clientes = ClienteBLL.getListClientes())

@cliente.route('/cliente/cadastrar', methods=['POST'])
def cadastrar():

    novo_cliente = Cliente()


    novo_cliente.nome = request.form['nome']
    novo_cliente.cpf_cnpj = request.form['cpf']
    novo_cliente.fone = request.form['telefone']
    novo_cliente.logradouro = ''
    novo_cliente.cep=''
    novo_cliente.numero = ''
    novo_cliente.bairro = ''
    novo_cliente.cidade = ''
    novo_cliente.uf='' 
    novo_cliente.observacao = ''
    
    

    ClienteBLL.setCliente(novo_cliente)
    
    return redirect(url_for('cliente.index_cliente'))

