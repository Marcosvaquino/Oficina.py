from dataclasses import dataclass
from datetime import datetime

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

