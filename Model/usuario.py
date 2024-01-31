from dataclasses import dataclass
import datetime
from typing import Any

@dataclass
class Usuario:
    id: int
    id_oficina: int
    nome: str
    login: str
    senha: str
    tipo: int
    ativo: int
    data_criacao: datetime
    data_atualizacao: datetime

    @staticmethod
    def from_dict(obj:Any)-> 'Usuario':
        id = obj.get("id")
        id_oficina = obj.get("id_oficina")
        nome = obj.get("nome")
        login = obj.get("login")
        senha = obj.get("senha")
        tipo = obj.get("tipo")
        ativo = obj.get("ativo")
        data_criacao = obj.get("data_criacao")
        data_atualizacao = obj.get("data_atualizacao")
        return Usuario(id,id_oficina,nome,login,senha,tipo,ativo,data_criacao,data_atualizacao)

    
