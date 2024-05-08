from dataclasses import dataclass
from enum import Enum
from Data.base import db

class TipoVeiculo(Enum):
    carro = 0
    moto = 1
    caminhao = 2

@dataclass
class Oficina(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    cnpj: int = db.Column(db.Integer)
    razao_social: str  = db.Column(db.String)
    nome_fantasia: str  = db.Column(db.String)

    # Informações de Contato:
    logradouro: str  = db.Column(db.String)
    numero: int = db.Column(db.Integer)
    bairro: str  = db.Column(db.String)
    cidade: str  = db.Column(db.String)
    uf: str  = db.Column(db.String(2))
    cep: int = db.Column(db.Integer)
    telefone: int = db.Column(db.Integer)
    email: str  = db.Column(db.String)

    # Responsáveis e Contato Comercial
    nome_responsavel: str  = db.Column(db.String)
    cargo_responsavel: str  = db.Column(db.String)
    telefone_comercial: int = db.Column(db.Integer)
    
    tipo_veiculo: int  = db.Column(db.Integer)

    def tipoVeiculo(self):
        return TipoVeiculo(self.tipo_veiculo)


    
    

   