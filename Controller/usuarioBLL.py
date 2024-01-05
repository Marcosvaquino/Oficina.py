from Model.usuario import Usuario

listaDeUsuarios = []

class UsuarioBLL():

    # Inserindo usuário na lista de usuários
    def setUsuario(usuario: Usuario):
        listaDeUsuarios.append(usuario)

    # Localizando o usuário na lista de usuários pelo CPF
    def getUsuario(id: int) -> Usuario:
        usuario = next((u for u in listaDeUsuarios if u.id == id), None)
        return usuario

    # Listando todos os usuários cadastrados
    def getListUsuarios() -> []:
        return listaDeUsuarios
