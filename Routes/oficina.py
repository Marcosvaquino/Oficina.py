from flask import Blueprint, redirect, render_template, session, url_for
from Model.oficina import Oficina
from Controller.oficinaBLL import *
from Controller.usuarioBLL import *


oficina = Blueprint('oficina',__name__, template_folder="View")


@oficina.route('/oficina')
def index_oficina():

    id_oficina = session['id_oficina']

    if not id_oficina:
        return redirect(url_for('index.getIndex'))

    return render_template('Oficina/oficina.html',oficina = OficinaBLL.getOficina(id_oficina), pagina='Oficina')