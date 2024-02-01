from dataclasses import dataclass
from datetime import datetime

@dataclass
class Oficina:
    # Informações Básicas da Empresa
    id:int
    nome:str
    CNPJ: str
    razao_social: str
    nome_fantasia: str

    # Informações de Contato:
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    CEP: str
    telefone: str
    email: str

    # Responsáveis e Contato Comercial
    nome_responsavel: str
    cargo_responsavel: str
    telefone_comercial: str
    email_comercial: str

    # Informações Financeiras:
    dados_bancarios: str
    