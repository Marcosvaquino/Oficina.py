from flask import session
from Model.usuario import Usuario,db

class UsuarioBLL():

    def login(login: str, senha: str) -> Usuario:
        return db.session.query(Usuario).filter_by(login=login, senha=senha).first()

    # Inserindo usuário na lista de usuários
    def setUsuario(usuario: Usuario):
        db.session.add(usuario)
        db.session.commit()
        
    # Localizando o usuário na lista de usuários pelo CPF
    def getUsuario(id: int) -> Usuario:
        return db.session.query(Usuario).filter_by(id=id).first()              

    # Listando todos os usuários cadastrados
    def getListUsuarios():
        return db.session.query(Usuario).all()
    
    def getListOperadores():
        return db.session.query(Usuario.id,Usuario.nome).filter_by(tipo=2).all()

    def getListUsuariosOficina():
        return db.session.query(Usuario).filter_by(id_oficina=session['id_oficina']).all()