from dataclasses import dataclass
import datetime
from enum import Enum
from typing import Any
from Data.base import db

class TipoUsuario(Enum):
    adminstrador = 1
    operador = 2
    caixa = 3

@dataclass
class Usuario(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_oficina: int = db.Column(db.Integer)
    nome: str = db.Column(db.String(50))
    login: str = db.Column(db.String(50))
    senha: str = db.Column(db.String(50))
    tipo: int = db.Column(db.Integer)
    ativo: bool = db.Column(db.Boolean)
    data_criacao: datetime = db.Column(db.DateTime)
    data_atualizacao: datetime = db.Column(db.DateTime)

    def tipoUsuario(self):
        return TipoUsuario(self.tipo)


    

       
