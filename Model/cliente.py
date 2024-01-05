from dataclasses import dataclass
from Model.carro import Carro
from typing import List


@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str
    logradouro: str
    cep: str
    numero: str
    bairro: str
    cidade: str
    uf: str
    observacoes: str
    carros: List[Carro]
