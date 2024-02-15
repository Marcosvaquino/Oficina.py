from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField
from wtforms.validators import Email, DataRequired

from Controller.clienteBLL import ClienteBLL

class LoginForm(FlaskForm):

    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])
    
class CadastroCarro(FlaskForm): 
         
        id = StringField('id',
                            id='id_create',
                            validators=[DataRequired()])
        
        id_oficina = StringField('id_oficina',
                        id='id_oficina_create',
                        validators=[DataRequired()])
        
        id_cliente = StringField('id_cliente',
                                id='id_cliente_create',
                                validators=[DataRequired()]) 
    
        placa = StringField('placa',
                            id='placa_create',
                            validators=[DataRequired()])          
    
        modelo = StringField('modelo',
                            id='modelo_create',
                            validators=[DataRequired()])          
    
        marca = StringField('marca',
                            id='marca_create',
                            validators=[DataRequired()])          
    
        cor = StringField('cor',
                            id='cor_create',
                            validators=[DataRequired()])          
    
        ano_fabricacao = StringField('ano_fabricacao',
                            id='ano_fabricacao_create',
                            validators=[DataRequired()])          
    
        ano_modelo = StringField('ano_modelo',
                            id='ano_modelo_create',
                            validators=[DataRequired()])          
    
        status = StringField('status',
                            id='status_create',
                            validators=[DataRequired()])          
    
        observacao = StringField('observacao',
                            id='observacao_create',
                            validators=[DataRequired()])          
    
        data_criacao = StringField('data_criacao',
                            id='data_criacao_create',
                            validators=[DataRequired()])          
    
        data_atualizacao = StringField('data_atualizacao',
                            id='data_atualizacao_create',
                            validators=[DataRequired()])

class CadastroOficina(FlaskForm):

    password = PasswordField('Senha',id='pwd_new',validators=[DataRequired()])
    password_confirm = PasswordField('Confirme a Senha',id='pwd_confirm',validators=[DataRequired()])
    
    email = StringField('Email',id='email',validators=[DataRequired(), Email()])
    cnpj = StringField('cnpj ou cpf',id='cnpj',validators=[DataRequired()])
    nome_fantasia = StringField('Nome Fantasia',id='nome_fantasia',validators=[DataRequired()])
    razao_social = StringField('Razão Social',id='razao_social',validators=[DataRequired()])
    logradouro = StringField('Logradouro',id='logradouro',validators=[DataRequired()])
    numero = StringField('Número',id='numero',validators=[DataRequired()])
    bairro = StringField('Bairro',id='bairro',validators=[DataRequired()])
    cidade = StringField('Cidade',id='cidade',validators=[DataRequired()])
    uf = StringField('UF',id='uf',validators=[DataRequired()])
    cep = StringField('CEP',id='cep',validators=[DataRequired()])
    telefone = StringField('Telefone',id='telefone',validators=[DataRequired()])

    nome_responsavel = StringField('Nome Responsável',id='nome_responsavel',validators=[DataRequired()])
class CadastroCliente(FlaskForm):

    fone = StringField('Telefone',id='fone',validators=[DataRequired()])
    cpf_cnpj = StringField('CPF ou CNPJ',id='cpf_cnpj',validators=[DataRequired()])
    nome = StringField('Nome',id='nome',validators=[DataRequired()])
    cep = StringField('CEP',id='cep',validators=[DataRequired()])
    logradouro = StringField('Logradouro',id='logradouro',validators=[DataRequired()])
    numero = StringField('Número',id='numero',validators=[DataRequired()])
    bairro = StringField('Bairro',id='bairro',validators=[DataRequired()])
    cidade = StringField('Cidade',id='cidade',validators=[DataRequired()])
    uf = StringField('UF',id='uf',validators=[DataRequired()])
    complemento = StringField('Complemento',id='complemento',validators=[DataRequired()])
    status = SelectField('Status',id='status',choices=[('1','Ativo'),('0','Inativo')],validators=[DataRequired()])
    observacao = StringField('Observação',id='observacao',validators=[DataRequired()])

class CadastroServico(FlaskForm):
         
        id = StringField('id',id='id',validators=[DataRequired()])
        id_oficina = StringField('id_oficina',id='id_oficina',validators=[DataRequired()])
        SelecionarCliente = SelectField('Selecionar Cliente',id='SelecionarCliente',choices= ClienteBLL.gerListClientesSelect,validators=[DataRequired()])
        SelecionarCarro = SelectField('Selecionar Carro',id='SelecionarCarro',validators=[DataRequired()])
        nome = StringField('Nome',id='nome',validators=[DataRequired()])
        descricao = StringField('Descrição',id='descricao',validators=[DataRequired()])
        valor = StringField('Valor',id='valor',validators=[DataRequired()])
        observacao = StringField('Observação',id='observacao',validators=[DataRequired()])
        data_criacao = StringField('Data de Criação',id='data_criacao',validators=[DataRequired()])
        data_atualizacao = StringField('Data de Atualização',id='data_atualizacao',validators=[DataRequired()])

