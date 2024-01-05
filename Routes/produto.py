from flask import Blueprint, redirect,render_template,request,url_for
from Model.produto import Produto
from Controller.produtoBLL import *

produto = Blueprint('produto',__name__,template_folder="View")

@produto.route('/produto')
def index_produto():
    return render_template('produto.html',produtos = ListadeProdutos)

@produto.route('/produto/cadastrar', methods=['POST'])
def cadastrar():

    codigo= request.form['codigo']
    descricao = request.form['descricao']
    preco= request.form['preco']
    precoCusto= request.form['precoCusto']
    estoque= request.form['estoque']
    tipo= request.form['tipo']
      
    novo_produto = Produto(1,1,codigo,descricao,preco,precoCusto,estoque,tipo,'','')

    ProdutoBLL.setProduto(novo_produto)
    
    return redirect(url_for('produto.index_produto'))

