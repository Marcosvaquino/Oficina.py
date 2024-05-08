from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField,  HiddenField,  StringField, PasswordField,SelectField, SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired

from Controller.usuarioBLL import UsuarioBLL
from Model.item_servico import StatusItem
from Model.ordem_servico import StatusOs, TipoServico, Prioridade

class LoginForm(FlaskForm):

    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])
    
class CadastroVeiculo(FlaskForm): 
         
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
class FormCliente(FlaskForm):

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
         
        id = HiddenField('id',id='id',validators=[DataRequired()])

        id_cliente = HiddenField('id_cliente',id='id_cliente',validators=[DataRequired()])
        id_veiculo = HiddenField('id_veiculo',id='id_veiculo',validators=[DataRequired()])
        
        fone = StringField('Contato Cliente*',id='fone', validators=[DataRequired()])
        nome = StringField('Nome*',id='nome',render_kw={"autocomplete": "on"}, validators=[DataRequired()])

        placa = StringField('Placa*',id='placa',render_kw={"autocomplete": "on"},validators=[DataRequired()])
        modelo = StringField('Modelo*',id='modelo',validators=[DataRequired()])
        ano = StringField('Ano*',id='ano',validators=[DataRequired()])

        data_entrada = DateField('Data de Entrada',id='data_entrada',default='',validators=[DataRequired()])
        data_previsao = DateField('Previsão de Entrega',id='data_previsao',default='',validators=[DataRequired()])

        tipo_servico = SelectField('Tipo de Serviço',id='tipo_servico',choices=[(enum.value,enum.name) for enum in TipoServico],validators=[DataRequired()])
        prioridade = SelectField('Prioridade',id='prioridade',choices=[(enum.value,enum.name) for enum in Prioridade],validators=[DataRequired()])
        status = SelectField('Status',id='status',choices=[(enum.value,enum.name) for enum in StatusOs],validators=[DataRequired()])
        quilometragem = StringField('Quilometragem',id='quilometragem',validators=[DataRequired()])

        descricao = TextAreaField('Descrição',id='descricao')
        valor = StringField('Valor',id='valor')
        
        data_criacao = StringField('Data de Criação',id='data_criacao')
        data_atualizacao = StringField('Data de Atualização',id='data_atualizacao')

        salvar = SubmitField('Salvar')

class FormItemServico(FlaskForm):

    id_item = HiddenField('id_item',id='id_item',validators=[DataRequired()])
    
    id_ordem_servico = HiddenField('id_ordem_servico',id='id_ordem_servico',validators=[DataRequired()])
    id_produto = HiddenField('id_produto',id='id_produto',validators=[DataRequired()])
    id_usuario = HiddenField('id_usuario',id='id_usuario',validators=[DataRequired()])

    codigo = StringField('Código',id='codigo',validators=[DataRequired()])
    nome_produto = StringField('Nome',id='nome',validators=[DataRequired()])

    status_item = SelectField('Status',id='status',choices=[(enum.value,enum.name) for enum in StatusItem],validators=[DataRequired()])
    select_usuario_item = SelectField('Operador',id='select_usuario',choices= UsuarioBLL.getListOperadores)

    valor_unitario = DecimalField('Valor Unitário',id='valor_unitario',validators=[DataRequired()])
    
    qtd = DecimalField('Quantidade',id='qtd',default=1.000,validators=[DataRequired()])

    desconto = DecimalField('Desconto',id='desconto',default=0.00)
    acrescimo = DecimalField('Acréscimo',id='acrescimo',default=0.00)
    
    descricao = StringField('Descrição',id='descricao')



