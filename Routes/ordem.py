from flask import Blueprint, jsonify, redirect,render_template,request, session,url_for
from Controller.form import CadastroServico, FormItemServico
from Controller.ordemServicoBLL import OrdemServicoBLL
from Controller.veiculoBLL import VeiculoBLL
from Model.item_servico import ItemServico
from Model.ordem_servico import OrdemServico
from Controller.oficinaBLL import OficinaBLL
from Controller.clienteBLL import *
from Model.veiculo import Veiculo

ordem = Blueprint('ordem',__name__,template_folder="View")

@ordem.route('/ordem', methods=['GET'])
@ordem.route('/ordem/<id>', methods=['GET'])
def indexOrdemServico(id:int=0):

    form = CadastroServico(request.form)
    formItem = FormItemServico(request.form)

    if int(id) > 0:
        ordem: OrdemServico = OrdemServicoBLL.getOrdemServico(id)
        cliente: Cliente = ClienteBLL.getClienteId(ordem.id_cliente)
        veiculo: Veiculo = VeiculoBLL.getVeiculoId(ordem.id_veiculo)
    else:
        ordem= OrdemServico()
        ordem.id = 0
        ordem.quilometragem = 0
        cliente = Cliente()
        cliente.nome=''
        cliente.fone=''
        veiculo = Veiculo()
        veiculo.placa=''
        veiculo.quilometragem=''
        veiculo.marca=''
        veiculo.modelo=''
        veiculo.ano_fabricacao=''
        veiculo.ano_modelo=''

    return render_template('Ordens/os.html',
                           pagina='Ordem de Serviço',
                           cliente=cliente ,
                           veiculo=veiculo,
                           os=ordem,
                           itens=ordem.itens(),
                           form=form,
                           formItem=formItem,)

@ordem.route('/ordem/cadastrar/<int:id>', methods=['POST'])
def cadastrar(id:int=0):

    if not session['id_oficina']:
        return redirect(url_for('index.getLogin'))

    id_oficina:int = session['id_oficina']
    
    if id > 0:
        ordem: OrdemServico = OrdemServicoBLL.getOrdemServico(id)
        cliente: Cliente = ClienteBLL.getClienteId(ordem.id_cliente)
    else:
        ordem= OrdemServico()
        ordem.id = 0
        ordem.quilometragem = 0
        cliente = Cliente()
        cliente.nome=''
        cliente.fone=''
        veiculo = Veiculo()
        veiculo.placa=''
        veiculo.quilometragem=''
        veiculo.marca=''
        veiculo.modelo=''
        veiculo.ano_fabricacao=''
        veiculo.ano_modelo=''

    if request.method == 'POST':               
        ordem.id_cliente = request.form['id_cliente']
        ordem.id_veiculo = request.form['id_veiculo']
        ordem.id_oficina = id_oficina
        ordem.id_usuario = session['id_usuario']
        ordem.status = '1'
        ordem.valor_pecas=0
        ordem.valor_servicos=0
        ordem.valor_desconto=0
        ordem.valor_acrescimo=0
        ordem.quilometragem = request.form['quilometragem']
        ordem.prioridade = request.form['prioridade']
        ordem.tipo_servico = request.form['tipo_servico']
        ordem.data_entrada = request.form['data_entrada']
        ordem.data_previsao = request.form['data_previsao']
        ordem.descricao=request.form['descricao']        

        if ordem.id == 0:
           id= OrdemServicoBLL.setOrdemServico(ordem)
        else:
           id= OrdemServicoBLL.updateOrdemServico(ordem)    

    return redirect('/ordem/{}'.format(id))

@ordem.route('/ordem/item', methods=['POST'])
def cadastrarItem():
    
    if request.method == 'POST':
        id_ordem = request.form['id_ordem_servico']
        id_produto = request.form['id_produto']
        id_usuario = session['id_usuario']
        qtd = request.form['qtd']
        valor_unitario = request.form['valor_unitario']
        desconto = request.form['desconto']
        acrescimo = request.form['acrescimo']
        descricao = request.form['descricao']

        item = ItemServico(id_ordem_servico=id_ordem,id_produto=id_produto,id_usuario=id_usuario,qtd=qtd,valor_unitario=valor_unitario,desconto=desconto,acrescimo=acrescimo,descricao=descricao)

        OrdemServicoBLL.setItemServico(item)    

    return redirect('/ordem/{}'.format(id_ordem))

