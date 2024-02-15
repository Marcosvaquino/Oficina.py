from flask import session
from Model.cliente import Cliente,db
class ClienteBLL():

    # Inserindo cliente na lista de clientes
    def setCliente(cliente: Cliente):
        db.session.add(cliente)
        db.session.commit()

    def updateCliente(cliente: Cliente):
        db.session.merge(cliente)
        db.session.commit()
        
    # Localizando o cliente na lista de clientes pelo CPF
    def getCliente(cpf: int) -> Cliente:
        return Cliente.query.filter_by(cpf=cpf).first()

    # Listando todos os clientes cadastrados
    def getListClientes():
        return Cliente.query.filter_by(id_oficina=session['id_oficina']).all()

    def gerListClientesSelect():
        clientes = db.session.query(Cliente).all()
        lista = []
        for cliente in clientes:
            lista.append((cliente.id,cliente.nome))
        return lista
