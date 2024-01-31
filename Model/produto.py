from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class Produto:
    id: int
    idFornecedor: int
    codigo: int
    descricao: str
    preco: float
    precoCusto: float
    estoque: int
    tipo: int
    dataCriacao: datetime
    dataAtualizacao: datetime

    @staticmethod
    def from_dict(obj:Any)-> 'Produto':
        id = obj.get("id")
        idFornecedor = obj.get("idFornecedor")
        codigo = obj.get("codigo")
        descricao = obj.get("descricao")
        preco = obj.get("preco")
        precoCusto = obj.get("precoCusto")
        estoque = obj.get("estoque")
        tipo = obj.get("tipo")
        dataCriacao = obj.get("dataCriacao")
        dataAtualizacao = obj.get("dataAtualizacao")
        return Produto(id,idFornecedor,codigo,descricao,preco,precoCusto,estoque,tipo,dataCriacao,dataAtualizacao)

