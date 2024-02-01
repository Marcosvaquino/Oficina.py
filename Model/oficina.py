from datetime import datetime
from typing import Any
from dataclasses import dataclass
from Data.base import db

@dataclass
class Oficina(db.Model):
    # Informações Básicas da Empresa
    id:int = db.Column(db.Integer, primary_key=True)
    cnpj: int = db.Column(db.Integer(14))
    razao_social: str  = db.Column(db.String)
    nome_fantasia: str  = db.Column(db.String)

    # Informações de Contato:
    logradouro: str  = db.Column(db.String)
    numero: int = db.Column(db.Integer(4))
    bairro: str  = db.Column(db.String)
    cidade: str  = db.Column(db.String)
    uf: str  = db.Column(db.String(2))
    cep: int = db.Column(db.Integer(8))
    telefone: int = db.Column(db.Integer)
    email: str  = db.Column(db.String)

    # Responsáveis e Contato Comercial
    nome_responsavel: str  = db.Column(db.String)
    cargo_responsavel: str  = db.Column(db.String)
    telefone_comercial: int = db.Column(db.Integer)
    email_comercial: str  = db.Column(db.String)

    # Informações Financeiras:
    dados_bancarios: str  = db.Column(db.String)


    @staticmethod
    def from_dict(obj:Any)-> 'Oficina':
        id = obj.get("id")
        cnpj = obj.get("CNPJ")
        razao_social = obj.get("razao_social")
        nome_fantasia = obj.get("nome_fantasia")
        logradouro = obj.get("logradouro")
        numero = obj.get("numero")
        bairro = obj.get("bairro")
        cidade = obj.get("cidade")
        uf = obj.get("uf")
        cep = obj.get("cep")
        telefone = obj.get("telefone")
        email = obj.get("email")
        nome_responsavel = obj.get("nome_responsavel")
        cargo_responsavel = obj.get("cargo_responsavel")
        telefone_comercial = obj.get("telefone_comercial")
        email_comercial = obj.get("email_comercial")
        dados_bancarios = obj.get("dados_bancarios")
        return Oficina(id,cnpj,razao_social,nome_fantasia,logradouro,numero,bairro,cidade,uf,cep,telefone,email,nome_responsavel,cargo_responsavel,telefone_comercial,email_comercial,dados_bancarios)