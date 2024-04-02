from flask import Blueprint, redirect,render_template,request,url_for
from Model.produto import Produto
from Controller.produtoBLL import *

produto = Blueprint('produto',__name__,template_folder="View")

@produto.route('/produto')
def index_produto():
    return render_template('Produtos/produto.html',produtos = ProdutoBLL.getListadeProdutos(), pagina='Produtos')

@produto.route('/produto/cadastrar', methods=['POST'])
def cadastrar():

    novo_produto = Produto()

    novo_produto.id_oficina= request.form['id_oficina']
    novo_produto.id_fornecedor= 0
    novo_produto.codigo= request.form['codigo']
    novo_produto.descricao = request.form['descricao']
    novo_produto.preco= request.form['preco']
    novo_produto.preco_custo= request.form['preco_custo']
    novo_produto.estoque= request.form['estoque']
    novo_produto.tipo= request.form['tipo']
      
    
    ProdutoBLL.setProduto(novo_produto)
    
    return redirect(url_for('produto.index_produto'))

