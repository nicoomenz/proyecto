from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.instrumentos import Instrumento
from flaskps.models.tipoInstrumento import TipoInstrumento
from flaskps.helpers.auth import authenticated
from flaskps.models.configuracion import Configuracion
from flaskps.models.user import User
import base64
from base64 import b64encode

def index():
    Instrumento.db = get_db()

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    pag= request.args.get('pagina')

    Configuracion.db = get_db()
    config = Configuracion.all()
    # rango= Instrumento.rangoFind(request.form,config['paginacion'])
    # pag,config['paginacion']
    instrumentos = Instrumento.all(pag, config['paginacion'])
    rango = Instrumento.rango(config['paginacion'])
    return render_template('instrumentos/index.html', instrumentos=instrumentos,pages=config['paginacion'],rango=rango,vista='instrumentos_index', permisos= permisos)
    # , instrumentos=instrumentos, rango=rango, pages=pag

def new():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    TipoInstrumento.db = get_db()
    tipoInstrumentos = TipoInstrumento.all()
    return render_template('instrumentos/new.html', tipoInstrumentos = tipoInstrumentos,permisos = permisos)


def create():
    Instrumento.db = get_db()
    # raise ValueError(request.form)
    if 'imagen' not in request.files:
        print('No esta la foto')
    #raise ValueError(image64)
    data = request.form

    codUnico = Instrumento.find_by_codigo(data['descripcionDeEstado'])

    if codUnico:
        flash("El codigo ya existe.")
        return redirect(url_for('instrumentos_new'))

    image=request.files['imagen']
    # raise ValueError(image)
    image64=base64.b64encode(image.read())
    Instrumento.create(request.form,image64)
    return redirect(url_for('instrumentos_index'))

def update():
    if not authenticated(session):
        abort(401)
    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    TipoInstrumento.db = get_db()
    tipoInstrumentos = TipoInstrumento.all()


    Instrumento.db = get_db()
    id_instrumento= request.args.get('id')
    instrumento = Instrumento.search(id_instrumento)
    return render_template('instrumentos/update.html', instrumentos=instrumento, tipoInstrumentos=tipoInstrumentos, permisos=permisos)

def modificar():
    if not authenticated(session):
        abort(401)

    Instrumento.db = get_db()

    id_instrumento = request.args.get('id')
    data = request.form
    codUnico = Instrumento.find_by_codigo(data['descripcionDeEstado'])

    if codUnico:
        flash("El codigo ya existe.")
        return redirect(url_for('instrumento_update'))
    Instrumento.modificar(data) #agarro los datos del formulario
    

    return redirect(url_for('instrumentos_index'))


def delete():
    Instrumento.db = get_db()
    id_instrumento= request.args.get('id')
    Instrumento.delete(id_instrumento)
    instrumentos = Instrumento.all()
    return render_template('instrumentos/index.html', instrumentos=instrumentos)

def find():


    pag= request.args.get('pagina')

    Configuracion.db = get_db()
    config = Configuracion.all()


    Instrumento.db =get_db()

    rango= Instrumento.rangoFind(request.form,config['paginacion'])

    instrumentos = Instrumento.find(request.form,pag,config['paginacion'])
    return render_template('instrumentos/index.html', instrumentos=instrumentos, pages=config['paginacion'],rango=rango)

def detail():
    id_instrumento = request.args.get('id')
    Instrumento.db =get_db()
    instrumento = Instrumento.obtenerId(id_instrumento)
    return render_template('instrumentos/show.html',instrumento=instrumento)


