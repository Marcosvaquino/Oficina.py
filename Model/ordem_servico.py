from dataclasses import dataclass
from datetime import datetime

@dataclass
class os:
    id: int
    id_carro: int
    id_cliente: int
    id_oficina: int
    id_usuario: int
    status: int
    valor_total: float
    valor_desconto: float
    valor_acrescimo: float
    observacoes: str
    data_previsao: datetime
    data_criacao: datetime
    data_atualizacao: datetime

class item_os:
    id: int
    id_os: int
    id_produto: int
    qtd: int
    valor_venda: float    
    