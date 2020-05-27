from flask import redirect, render_template, request, url_for, session, abort, flash
import requests
import json
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.barrio import Barrio
from flaskps.models.escuela import Escuela
from flaskps.models.student import Estudiante
from flaskps.models.rol import Rol
from flaskps.models.barrio import Barrio
from flaskps.models.escuela import Escuela
from flaskps.models.nivel import Nivel
from flaskps.models.responsable import Responsable
from flaskps.models.configuracion import Configuracion
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User

def new():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    
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
    
    Rol.db = get_db()
    roles = Rol.all()

    Responsable.db = get_db()
    responsables = Responsable.all()

    Nivel.db = get_db()
    niveles = Nivel.all()

    Barrio.db = get_db()
    barrios = Barrio.all()

    Escuela.db = get_db()
    escuelas = Escuela.all()
 
    return render_template('student/new.html',escuelas= escuelas, barrios= barrios, roles=roles, niveles=niveles, permisos=permisos,documentos=documentos,localidades=localidades,responsables=responsables)

def show():
    if not authenticated(session):
        abort(401)

    Estudiante.db = get_db()
    permisos = Estudiante.misPermisos(session['id'])
    
    Nivel.db = get_db()
    niveles = Nivel.all()

    Barrio.db = get_db()
    barrios = Barrio.all()

    Escuela.db = get_db()
    escuelas = Escuela.all()
    
    Responsable.db = get_db()
    responsables = Responsable.all()
    
    Estudiante.db = get_db()
    id_estudiante= request.args.get('id')
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
    student = Estudiante.search(id_estudiante)
    id_responsable = Estudiante.searchIdResponsable(id_estudiante)
    id_genero = Estudiante.searchIdGender(id_estudiante)
    id_nivel = Estudiante.searchIdNivel(id_estudiante) 

    escuelas = Escuela.all()
    barrios = Barrio.all()

    return render_template('student/show.html',id_nivel = id_nivel, id_responsable=id_responsable, estudiante=student, id_genero= id_genero, documentos= documentos, localidades= localidades, niveles=niveles,permisos=permisos, barrios=barrios, escuelas=escuelas, responsables=responsables)

def validateCreateStudent(data):
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
   # raise ValueError(page)
    Estudiante.db = get_db()
    estudiantes = Estudiante.all(page,config['paginacion'])
    rango= Estudiante.rangoAll(config['paginacion'])


    return render_template('student/index.html', estudiantes=estudiantes, pages=config['paginacion'],rango=rango,vista='student_index', permisos = permisos)

def create():
    if not authenticated(session):
        abort(401)
    page = request.args.get('pagina')

    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    Configuracion.db = get_db()
    config = Configuracion.all()

    data = request.form

    #User.db = get_db()
    #user = User.find_by_email(data['email'])
    
    Estudiante.db = get_db()
    estudiante = Estudiante.find_by_documento(data['numero_doc'])

    estudiantes = Estudiante.all(page,config['paginacion'])
    rango = Estudiante.rangoAll(config['paginacion'])

    User.db = get_db()
    userDoc= User.find_by_documento(data['numero_doc'])
    
    #if  validateCreateUser(data) == False:
    #   flash("Todos los campos son obligatorios.")
    #   return redirect(url_for('student_new', estudiante=estudiante))

    if userDoc:
        flash("El documento ya existe.")
        return redirect(url_for('student_new', estudiante=estudiante))

    if estudiante:
        flash("El documento ya existe.")
        return redirect(url_for('student_new', estudiante=estudiante))

    Estudiante.create(data) #agarro los datos del formulario
    #return render_template('student/index.html', estudiantes=estudiantes, pages=config['paginacion'],rango=rango,vista='student_index', permisos = permisos)
    return redirect(url_for('student_index',pagina=0))


def update():
    if not authenticated(session):
        abort(401)

    Estudiante.db = get_db()
    permisos = User.misPermisos(session['id'])
    
    Nivel.db = get_db()
    niveles = Nivel.all()

    id_student= request.args.get('id')
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

    estudiante = Estudiante.search(id_student)
    id_genero = Estudiante.searchIdGender(id_student)
    id_responsable = Estudiante.searchIdResponsable(id_student)
    id_nivel = Estudiante.searchIdNivel(id_student)

    responsables = Estudiante.obtenerResponsables()
    escuelas = Estudiante.obtenerEscuelas()
    barrios= Estudiante.obtenerBarrios()
    #raise ValueError(request.args.get('id'))
    estudiante = Estudiante.search(id_student)
    return render_template('student/update.html',id_responsable=id_responsable, id_nivel=id_nivel, escuelas=escuelas, barrios=barrios, responsables=responsables, estudiante=estudiante,  documentos= documentos, id_genero= id_genero, localidades= localidades, niveles=niveles,permisos=permisos)

    

def modificar():
    if not authenticated(session):
        abort(401)

    permisos = Estudiante.misPermisos(session['id'])

    pag= request.args.get('pagina')
    data = request.form
    Configuracion.db = get_db()
    config = Configuracion.all()

    Rol.db = get_db()
    roles = Rol.all()
    pag= request.args.get('pagina')

    Nivel.db = get_db()
    niveles = Nivel.all()

    Estudiante.db = get_db()

    Estudiante.modificar(request.form,pag,config['paginacion']) #agarro los datos del formulario
    
    estudiante = Estudiante.all(pag,config['paginacion'])
    rango= Estudiante.rangoAll(config['paginacion'])


    return redirect(url_for('student_index',pagina=0))

def find():
    if not authenticated(session):
        abort(401)

    pag= request.args.get('pagina')
    # name= request.args.get('name')
    permisos = User.misPermisos(session['id'])

    User.db = get_db()
    Configuracion.db = get_db()
    config = Configuracion.all()

    rango= User.rangoFind(request.form,config['paginacion'])

    users = User.find(request.form,pag,config['paginacion'])
    return render_template('user/index.html', users=users, pages=config['paginacion'],rango=rango,vista='user_find',permisos=permisos)

def delete():
    if not authenticated(session):
        abort(401)  


    permisos = User.misPermisos(session['id'])
    pag= request.args.get('pagina')

    User.db = get_db()
    id_user= request.args.get('id')

    Estudiante.db = get_db()
    id_student= request.args.get('id')

    
    Configuracion.db = get_db()
    config = Configuracion.all()
    pag= request.args.get('pagina')

    user = User.all(pag,config['paginacion'])

    rango= User.rangoAll(config['paginacion'])

    Estudiante.delete(id_student,pag,config['paginacion'])
    estudiantes=Estudiante.all(pag,config['paginacion'])
    return render_template('student/index.html', estudiantes=estudiantes, pages=config['paginacion'],rango=rango,vista='student_delete',permisos=permisos)

