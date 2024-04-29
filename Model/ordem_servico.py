from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from Data.base import db
from Model.cliente import Cliente
from Model.item_servico import ItemServico
from Model.usuario import Usuario
from Model.veiculo import Veiculo

class StatusOs(Enum):
    pendente=0
    andamento=1
    finalizado=2
    cancelado=3
    peca=4
    cliente=5   
    pagamento=6
    retirada=7

class TipoServico(Enum):
    revisao=0
    retorno=1
    garantia=2
    acessorio=3
    orcamento=4
    funilaria=5
    manutencao=6
    terceiros=7
    outros=8
    
class Prioridade(Enum):
    baixa=0
    media=1
    alta=2
    urgente=3

@dataclass
class OrdemServico(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    numero_os: int = db.Column(db.Integer,default=0)

    id_veiculo: int = db.Column(db.Integer)
    id_cliente: int = db.Column(db.Integer)
    id_oficina: int = db.Column(db.Integer) 
    id_usuario: int = db.Column(db.Integer)

    status: int = db.Column(db.Integer)
    valor_pecas: float = db.Column(db.Float)
    valor_servicos: float = db.Column(db.Float)
    valor_desconto: float = db.Column(db.Float)
    valor_acrescimo: float = db.Column(db.Float)
    descricao: str = db.Column(db.String(200))
    tipo_servico: str = db.Column(db.Integer)
    prioridade: int = db.Column(db.Integer)
    quilometragem: int = db.Column(db.Integer)

    data_entrada: datetime = db.Column(db.DateTime)
    data_previsao: datetime = db.Column(db.DateTime)

    data_criacao: datetime = db.Column(db.DateTime, default=datetime.now())
    data_atualizacao: datetime = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def veiculo(self):
        return Veiculo.query.get(self.id_veiculo)
    def cliente(self):
        return Cliente.query.get(self.id_cliente)
    def usuario(self):
        return Usuario.query.get(self.id_usuario)    
    def statusOs(self):
        return StatusOs(self.status)    
    def tipoServico(self):
        return TipoServico(self.tipo_servico)
    def prioridadeOs(self):
        return Prioridade(self.prioridade)
    def itens(self):
        return ItemServico.query.filter_by(id_ordem_servico=self.id).all()
    def valor_total(self):
        return self.valor_pecas + self.valor_servicos + self.valor_acrescimo - self.valor_desconto
    
