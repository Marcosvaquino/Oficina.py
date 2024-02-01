from flask import Blueprint, redirect,render_template,request,url_for
from Model.cliente import Cliente
from Controller.clienteBLL import ClienteBLL

cliente = Blueprint('cliente',__name__,template_folder="View")

@cliente.route('/cliente')
def index_cliente():
    return render_template('cliente.html',clientes = ClienteBLL.getListClientes())

@cliente.route('/cliente/cadastrar', methods=['POST'])
def cadastrar():

    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    logradouro = ''
    cep=''
    numero = ''
    bairro = ''
    cidade = ''
    uf='' 
    observacoes = ''
    carros=[]   

    novo_cliente = Cliente(1,nome,cpf,telefone,logradouro,cep,numero,bairro,cidade,uf,observacoes,carros)

    ClienteBLL.setCliente(novo_cliente)
    
    return redirect(url_for('cliente.index_cliente'))

