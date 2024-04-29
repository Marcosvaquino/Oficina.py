from flask import Blueprint,  render_template,request,redirect,url_for,session
from Controller.ordemServicoBLL import OrdemServicoBLL
from Controller.usuarioBLL import UsuarioBLL
from Controller.oficinaBLL import OficinaBLL
from Model.usuario import Usuario
from Controller.form import CadastroOficina, LoginForm
from Model.oficina import Oficina

index = Blueprint('index', __name__)

@index.route('/', methods=['GET','POST'])
def getLogin():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']
        
        # Locate user
        logado:Usuario = UsuarioBLL.login(username,password)
        
        # Check the password
        if logado:
           session['username'] = username
           session['id_oficina'] = logado.id_oficina
           session['id_usuario'] = logado.id

           return redirect(url_for('index.getIndex'))

        # Something (user or pass) is not ok
        return render_template('Login/login.html',
                               msg='Usuário ou senha incorretos',
                               form=login_form)
    else:
        return render_template('Login/login.html',form=login_form)
    

@index.route('/index', methods=['GET'])
def getIndex():
    if session.get('username'):       
        return render_template('index.html',ordens= OrdemServicoBLL.getOrdensServico(),  segment='index')
    else:
        return redirect(url_for('index.getLogin')) 

    
    
@index.route('/registrar', methods=['GET','POST'])
def register():

    create_account_form = CadastroOficina(request.form)
   
    if 'register' in request.form:

        pswd = request.form['password']
        pswd2 = request.form['password_confirm']

        if pswd != pswd2:
            return render_template('Login/register.html',
                                   msg='As senhas não conferem',
                                   success=False,
                                   form=create_account_form)

        nova_oficina = Oficina()

        nova_oficina.cnpj = request.form['cnpj']
        nova_oficina.nome_fantasia = request.form['nome_fantasia']
        nova_oficina.email = request.form['email']
        nova_oficina.dados_bancarios = pswd #campo de dados bancarios foi usado para senha      

        # Check usename exists
        user = OficinaBLL.consultaCNPJ(nova_oficina.cnpj)
        if user:
            return render_template('Login/register.html',
                                   msg='Ja existe uma conta cadastrada com esse CPF / CNPJ',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = OficinaBLL.consultaEmail(nova_oficina.email)
        if user:
            return render_template('Login/register.html',
                                   msg='Ja existe uma conta com esse email',
                                   success=False,
                                   form=create_account_form)
     
        if OficinaBLL.setOficina(nova_oficina):
            return render_template('Login/register.html',
                               msg='Usuário registrado com sucesso',
                               success=True,
                               form=create_account_form)
        else:
            return render_template('Login/register.html',
                               msg='Erro ao registrar usuário',
                               success=False,
                               form=create_account_form)
    else:
        return render_template('Login/register.html', form=create_account_form)


@index.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('id_oficina', None)
    return redirect(url_for('index.getLogin'))

