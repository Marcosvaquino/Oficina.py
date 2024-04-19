import os
from flask import Flask
from Data.base import connectionString, db


from config import config_dict

from Routes.index import index
from Routes.veiculo import veiculo
from Routes.cliente import cliente
from Routes.produto import produto
from Routes.usuario import usuario
from Routes.ordem import ordem
from Routes.oficina import oficina

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')



app = Flask(__name__,template_folder="View")
app.config['SQLALCHEMY_DATABASE_URI'] = connectionString()

db.init_app(app)
app.config.from_object(app_config)

app.register_blueprint(veiculo)
app.register_blueprint(cliente)
app.register_blueprint(produto)
app.register_blueprint(usuario)
app.register_blueprint(oficina)
app.register_blueprint(index)
app.register_blueprint(ordem)

app.run(debug=True)
