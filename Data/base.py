from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

host='177.234.148.10'
user = 'prem0867_oficina'
senha='ULr4Eu4tn8EtbCG'
bd='prem0867_oficina'

def connectionString()->str:
    return f"mysql://{user}:{senha}@{host}/{bd}"


