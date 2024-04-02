from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

host='187.33.241.16'
user = 'prem0867_oficina'
senha='ULr4Eu4tn8EtbCG'
bd='prem0867_oficina'

def connectionString()->str:
    return f"mysql://{user}:{senha}@{host}/{bd}"


