from Model.cliente import Cliente,db
class ClienteBLL():

    # Inserindo cliente na lista de clientes
    def setCliente(cliente: Cliente):
        db.session.add(cliente)
        db.session.commit()
        
    # Localizando o cliente na lista de clientes pelo CPF
    def getCliente(cpf: int) -> Cliente:
        return db.session.query(Cliente).filter_by(cpf=cpf).first()

    # Listando todos os clientes cadastrados
    def getListClientes() -> []:
        db.session.query(Cliente).all()
