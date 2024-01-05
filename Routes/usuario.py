from flask import Blueprint, redirect,render_template,request,url_for
from Model.usuario import Usuario
from Controller.usuarioBLL import *

usuario = Blueprint('usuario',__name__,template_folder="View")

@usuario.route('/usuario')
def index_usuario():
    return render_template('usuario.html',usuarios = listaDeUsuarios)

@usuario.route('/usuario/cadastrar', methods=['POST'])
def cadastrar():
 
  login = request.form['login']
  senha = request.form['senha']
        
  novo_usuario = Usuario(login,senha)

  UsuarioBLL.setUsuario(novo_usuario)
    
  return redirect(url_for('usuario.index_usuario'))

