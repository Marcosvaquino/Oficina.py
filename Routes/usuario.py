
from flask import Blueprint, redirect,render_template, request, url_for
from Model.usuario import Usuario
from Controller.usuarioBLL import *

usuario = Blueprint('usuario',__name__,template_folder="View")

@usuario.route('/usuario')
def index_usuario():
    return render_template('Usuarios/usuario.html',usuarios = UsuarioBLL.getListUsuarios(), pagina='Usuarios')

@usuario.route('/usuario/cadastrar', methods=['POST'])
def cadastrar():

  novo_usuario = Usuario()
 
  novo_usuario.id_oficina= request.form['id_oficina']
  novo_usuario.nome = request.form['nome']
  novo_usuario.login = request.form['login']
  novo_usuario.senha = request.form['senha']
  novo_usuario.tipo = request.form['tipo']
  novo_usuario.ativo = request.form['ativo']
        
  
  UsuarioBLL.setUsuario(novo_usuario)
    
  return redirect(url_for('usuario.index_usuario'))

