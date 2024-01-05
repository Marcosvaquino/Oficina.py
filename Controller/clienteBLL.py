from Model.cliente import Cliente

listaDeClientes = []

class ClienteBLL():

    # Inserindo cliente na lista de clientes
    def setCliente(cliente: Cliente):
        listaDeClientes.append(cliente)

    # Localizando o cliente na lista de clientes pelo CPF
    def getCliente(cpf: int) -> Cliente:
        cliente = next((c for c in listaDeClientes if c.cpf == cpf), None)
        return cliente

    # Listando todos os clientes cadastrados
    def getListClientes() -> []:
        return listaDeClientes
