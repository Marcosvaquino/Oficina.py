from dataclasses import dataclass
from enum import Enum
from Data.base import db
from Model.produto import Produto
from Model.usuario import Usuario

class StatusItem(Enum):
    pendente=0
    concluido=1
    cancelado=2

@dataclass
class ItemServico(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_ordem_servico: int = db.Column(db.Integer)
    id_produto: int = db.Column(db.Integer)
    id_usuario: int = db.Column(db.Integer)
    status_item: int = db.Column(db.Integer)
    qtd: float = db.Column(db.Float)
    valor_unitario: float = db.Column(db.Float)
    desconto: float = db.Column(db.Float)
    acrescimo: float = db.Column(db.Float)
    descricao: str = db.Column(db.String(200))

    def statusItem(self):
        return StatusItem(self.status_item)

    def produto(self):
        return Produto.query.get(self.id_produto)
    
    def usuario(self):
        return Usuario.query.get(self.id_usuario)

    def valor_total(self):
        return (self.qtd * self.valor_unitario) + self.acrescimo - self.desconto
    
