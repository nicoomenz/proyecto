from flask import redirect, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.ciclo import Ciclo
from flaskps.models.taller import Taller
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User

def index():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    Ciclo.db = get_db()
    ciclos = Ciclo.all()
    return render_template('ciclo/index.html', ciclos=ciclos, permisos=permisos)

def new():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    Ciclo.db = get_db()
    ciclos = Ciclo.all()

    return render_template('ciclo/new.html',ciclos=ciclos,permisos=permisos)

def create():

    data=request.form
    Ciclo.db=get_db()


    Ciclo.create(data)
    return redirect(url_for('ciclo_index'))

def show():

    permisos = User.misPermisos(session['id'])
    Ciclo.db = get_db()
    ciclos = Ciclo.all()
    id_ciclo = request.args.get('id')
    ciclo = Ciclo.searchCiclo(id_ciclo)
    return render_template('ciclo/show.html', ciclo=ciclo, permisos=permisos)

def asignar():
    permisos = User.misPermisos(session['id'])
    Ciclo.db=get_db()
    ciclos = Ciclo.all()

    Taller.db=get_db()
    talleres=Taller.all()
    return render_template('ciclo/asignarTaller.html',ciclos=ciclos,talleres=talleres, permisos=permisos)

def add():

    data = request.form
    
    Ciclo.db=get_db()
    
    Ciclo.agregarTaller(data)
    return redirect(url_for('ciclo_index'))

def update():
    if not authenticated(session):
        abort(401)
    permisos = User.misPermisos(session['id'])
    id_ciclo = request.args.get('id')

    Ciclo.db = get_db()
    ciclo = Ciclo.search(id_ciclo)

    return render_template('ciclo/update.html',ciclo=ciclo, permisos=permisos)

def modificar():
    if not authenticated(session):
        abort(401)
    
    pag= request.args.get('pagina')
    data = request.form

    pag= request.args.get('pagina')

    Ciclo.db = get_db()
    Ciclo.modificar(request.form) #agarro los datos del formulario

    return redirect(url_for('ciclo_index'))



def delete():
    if not authenticated(session):
        abort(401)  

    id_ciclo=request.args.get('id')

    Ciclo.db=get_db()
    Ciclo.delete(id_ciclo)

    return redirect(url_for('ciclo_index'))