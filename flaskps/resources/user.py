from flask import redirect, render_template, request, url_for, session, abort, flash
import requests
import json
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.rol import Rol
from flaskps.models.nivel import Nivel
from flaskps.models.configuracion import Configuracion
from flaskps.models.student import Estudiante
from flaskps.helpers.auth import authenticated


def validateCreateUser(data):
    if data['first_name'] == "":
        return False
    if data['last_name'] == "":
        return False
    if data['fecha_nac'] == "":
        return False
    if data['numero_doc'] == "":
        return False
    if data['domicilio'] == "":
        return False
    if data['telefono'] == "":
        return False
    if data['email'] == "":
        return False
    if data['password'] == "":
        return False
    return True

def index():
    if not authenticated(session):
        abort(401)
    page= request.args.get('pagina')


    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    Configuracion.db = get_db()
    config = Configuracion.all()

    User.db = get_db()
    users = User.all(page,config['paginacion'])
    rango= User.rangoAll(config['paginacion'])

    return render_template('user/index.html', users=users, pages=config['paginacion'],rango=rango,vista='user_index',permisos=permisos)


def new():
    if not authenticated(session):
        abort(401)


    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    
    Rol.db = get_db()
    roles = Rol.all()

    #API de documentos
    response = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    if response.status_code == 200:
        doc = response.text
        documentos = json.loads(doc)
        #raise ValueError(documentos)

    #API de localidades
    response2 = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    if response2.status_code == 200:
        loc = response2.text
        localidades = json.loads(loc)
        #raise ValueError(localidades)


    return render_template('user/new.html', roles=roles, documentos=documentos, localidades=localidades, permisos= permisos)
 

def create():
    if not authenticated(session):
        abort(401)
    page = request.args.get('pagina')

    permisos = User.misPermisos(session['id'])

    Configuracion.db = get_db()
    config = Configuracion.all()
    
    data = request.form
    
    Estudiante.db = get_db()
    estudiante = Estudiante.find_by_documento(data['numero_doc'])


    User.db = get_db()
    user = User.find_by_email(data['email'])
    userDoc= User.find_by_documento(data['numero_doc'])

    users = User.all(page,config['paginacion'])
    rango= User.rangoAll(config['paginacion'])
    
    if  validateCreateUser(data) == False:
        flash("Todos los campos son obligatorios.")
        return redirect(url_for('user_new', user=user))

    if user:
        flash("El email ya existe.")
        return redirect(url_for('user_new', user=user))

    if estudiante:
        flash("El documento ya existe.")
        return redirect(url_for('user_new', user=user))

    if userDoc:
        flash("El documento ya existe.")
        return redirect(url_for('user_new', user=user))


    User.create(data) #agarro los datos del formulario
    return redirect (url_for('user_index', pagina=0))

def show():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    
    Rol.db = get_db()
    roles = Rol.all()

    Nivel.db = get_db()
    niveles = Nivel.all()

    User.db = get_db()
    id_user= request.args.get('id')
    pag= request.args.get('pagina')

    #API de documentos
    response = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    if response.status_code == 200:
        doc = response.text
        documentos = json.loads(doc)
        #raise ValueError(documentos)

    #API de localidades
    response2 = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    if response2.status_code == 200:
        loc = response2.text
        localidades = json.loads(loc)

    #raise ValueError(request.args.get('id'))
    user = User.search(id_user)
    id_genero = User.searchIdGender(id_user)
    id_rol = User.searchIdRol(id_user)
    return render_template('user/show.html', id_rol=id_rol,users=user, id_genero= id_genero, documentos= documentos, localidades= localidades, roles=roles, niveles=niveles,permisos=permisos)


def update():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    
    Rol.db = get_db()
    roles = Rol.all()

    Nivel.db = get_db()
    niveles = Nivel.all()

    User.db = get_db()
    id_user= request.args.get('id')
    pag= request.args.get('pagina')

    #API de documentos
    response = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    if response.status_code == 200:
        doc = response.text
        documentos = json.loads(doc)
        #raise ValueError(documentos)

    #API de localidades
    response2 = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    if response2.status_code == 200:
        loc = response2.text
        localidades = json.loads(loc)

    #raise ValueError(request.args.get('id'))
    user = User.search(id_user)
    id_genero = User.searchIdGender(id_user)
    id_rol = User.searchIdRol(id_user)
    return render_template('user/update.html', id_rol=id_rol,users=user, id_genero= id_genero, documentos= documentos, localidades= localidades, roles=roles, niveles=niveles,permisos=permisos)

def modificar():
    if not authenticated(session):
        abort(401)

    permisos = User.misPermisos(session['id'])
    
    pag= request.args.get('pagina')
    data = request.form
    Configuracion.db = get_db()
    config = Configuracion.all()

    Rol.db = get_db()
    roles = Rol.all()
    pag= request.args.get('pagina')

    Nivel.db = get_db()
    niveles = Nivel.all()

    User.db = get_db()

    User.modificar(request.form,pag,config['paginacion'],) #agarro los datos del formulario
    
    users = User.all(pag,config['paginacion'])
    rango= User.rangoAll(config['paginacion'])

    return redirect (url_for('user_index', pagina=0))

def active():
    if not authenticated(session):
        abort(401)
    pag= request.args.get('pagina')

    User.db = get_db()
    # users = User.active()

    Configuracion.db = get_db()
    config = Configuracion.all()

    users = User.active(pag,config['paginacion'])


    rango= User.rangoActive(config['paginacion'])

    return render_template('user/index.html', users=users, pages=config['paginacion'],rango=rango,vista='user_active')

def bloq():
    if not authenticated(session):
        abort(401)

    pag= request.args.get('pagina')

    User.db = get_db()
    
    Configuracion.db = get_db()
    config = Configuracion.all()

    users = User.bloq(pag,config['paginacion'])

    rango= User.rangoBloq(config['paginacion'])

    return render_template('user/index.html', users=users, pages=config['paginacion'],rango=rango,vista='user_bloq')


def find():
    if not authenticated(session):
        abort(401)

    pag= request.args.get('pagina')
    # name= request.args.get('name')


    User.db = get_db()
    Configuracion.db = get_db()
    config = Configuracion.all()

    rango= User.rangoFind(request.form,config['paginacion'])

    users = User.find(request.form,pag,config['paginacion'])
    return render_template('user/index.html', users=users, pages=config['paginacion'],rango=rango,vista='user_find')


def delete():
    if not authenticated(session):
        abort(401)  

    permisos = User.misPermisos(session['id'])
    pag= request.args.get('pagina')

    User.db = get_db()
    id_user= request.args.get('id')
    
    Configuracion.db = get_db()
    config = Configuracion.all()

    user = User.all(pag,config['paginacion'])

    rango= User.rangoAll(config['paginacion'])

    User.delete(id_user,pag,config['paginacion'])

    return render_template('user/index.html', users=user, pages=config['paginacion'],rango=rango,vista='user_find', permisos=permisos)


def docentes():
    if not authenticated(session):
        abort(401)  

    User.db = get_db()
    id_taller= request.args.get('id')
    docentes = User.docentes(id_taller)

    return render_template('user/docentesAsignados.html',docentes=docentes)

