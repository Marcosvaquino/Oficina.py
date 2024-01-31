from typing import Any
from dataclasses import dataclass

@dataclass
class Carro:
    id:int
    id_oficina:int
    id_cliente:int
    placa: str
    modelo:str
    marca:str
    cor:str
    ano_fabricacao:int
    ano_modelo:int
    status:int
    observacao:str
    data_criacao:str
    data_atualizacao:str

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
