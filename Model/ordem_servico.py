import enum
from dataclasses import dataclass
from datetime import datetime
from Data.base import db

class status_os(enum.Enum):
    pendente=0
    andamento=1
    finalizado=2
    cancelado=3
    peca=4
    cliente=5   
    pagamento=6
    retirada=7

@dataclass
class os(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_carro: int = db.Column(db.Integer)
    id_cliente: int = db.Column(db.Integer)
    id_oficina: int = db.Column(db.Integer) 
    id_usuario: int = db.Column(db.Integer)
    status: int = db.Column(db.Integer)
    valor_total: float = db.Column(db.Float)
    valor_desconto: float = db.Column(db.Float)
    valor_acrescimo: float = db.Column(db.Float)
    observacoes: str = db.Column(db.String(200))
    data_previsao: datetime = db.Column(db.DateTime)
    data_criacao: datetime = db.Column(db.DateTime)
    data_atualizacao: datetime = db.Column(db.DateTime)

class item_os(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_os: int = db.Column(db.Integer)
    id_produto: int = db.Column(db.Integer)
    qtd: int = db.Column(db.Integer)    
    valor_venda: float = db.Column(db.Float) 



    