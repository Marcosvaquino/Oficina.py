from typing import Any
from dataclasses import dataclass
from Data.base import db
@dataclass
class Carro(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    id_oficina:int = db.Column(db.Integer)
    id_cliente:int = db.Column(db.Integer)
    placa: str = db.Column(db.String(7))
    modelo:str = db.Column(db.String(50))
    marca:str = db.Column(db.String(50))
    cor:str = db.Column(db.String(50))
    ano_fabricacao:int = db.Column(db.Integer)
    ano_modelo:int = db.Column(db.Integer) 
    status:int = db.Column(db.Integer)
    observacao:str = db.Column(db.String(200))
    data_criacao:str = db.Column(db.DateTime)
    data_atualizacao:str = db.Column(db.DateTime)

    @staticmethod
    def from_dict(obj:Any)-> 'Carro':
        id = obj.get("id")
        id_oficina = obj.get("id_oficina")
        id_cliente = obj.get("id_cliente")
        placa = obj.get("placa")
        modelo = obj.get("modelo")
        marca = obj.get("marca")
        cor = obj.get("cor")
        ano_fabricacao = obj.get("ano_fabricacao")
        ano_modelo = obj.get("ano_modelo")
        status = obj.get("status")
        observacao = obj.get("observacao")
        data_criacao = obj.get("data_criacao")
        data_atualizacao = obj.get("data_atualizacao")
        return Carro(id,id_oficina,id_cliente,placa,modelo,marca,cor,ano_fabricacao,ano_modelo,status,observacao,data_criacao,data_atualizacao)
