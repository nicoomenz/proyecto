from flask import redirect, render_template, request, url_for, session, abort, flash
import requests
import json
import datetime
from flaskps.db import get_db
from flaskps.models.ciclo import Ciclo
from flaskps.models.estudiante_taller import Estudiante_taller
from flaskps.models.docente_taller import Docente_taller
from flaskps.models.taller import Taller
from flaskps.models.student import Estudiante
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User
from flaskps.models.dia import Dia
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller
from flaskps.models.nucleo import Nucleo
from flaskps.models.horario import Horario
from flaskps.models.configuracion import Configuracion



def index():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])


    Horario.db = get_db()

    horarios = Horario.all() #Se hace un INNER JOIN con ciclo_lectivo y talleres
    Nucleo.db = get_db()
    nucleos = Nucleo.all() 
    Dia.db = get_db()
    dias = Dia.all()
    return render_template('horario/index.html', horarios=horarios, nucleos = nucleos, dias=dias, permisos=permisos)

def new():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])

        
    Ciclo_lectivo_taller.db = get_db()
    ciclos_talleres = Ciclo_lectivo_taller.all()

    Nucleo.db = get_db()
    nucleos = Nucleo.all()

    Dia.db = get_db()
    dias = Dia.all()

    return render_template('horario/new.html', permisos = permisos, nucleos = nucleos, dias= dias, ciclos_talleres= ciclos_talleres)

def create():
    if not authenticated(session):
        abort(401)
    page = request.args.get('pagina')

    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    Configuracion.db = get_db()
    config = Configuracion.all()

    data = request.form

    Horario.db = get_db()
    repetido = Horario.select_horario_repetido(data)

    if repetido:
        flash("El horario ya existe.")
        return redirect(url_for('horario_new'))


    Horario.create(data) #agarro los datos del formulario
    return redirect (url_for('home_index', pagina=0))

def show():
    User.db = get_db() 
    permisos = User.misPermisos(session['id'])
    id_horario = request.args.get('id')
    Horario.db = get_db()
    horarios = Horario.all()
    horario = Horario.searchHorario(id_horario)

    Nucleo.db = get_db()
    nucleos = Nucleo.all()

    Dia.db = get_db()
    dias = Dia.all()
    return render_template('horario/show.html', horario=horario, nucleos= nucleos, dias= dias, permisos=permisos)

def asistencia():
    User.db = get_db() 
    permisos = User.misPermisos(session['id'])

    id_horario = request.args.get('id')
    Horario.db=get_db()
    horario = Horario.searchHorario(id_horario)
    alumnos=Horario.alumnos_asignados(id_horario)
    id_taller = request.args.get('id_taller')
    taller = Taller.searchTaller(id_taller)
    #fechaActual = datetime.date.today()


    return render_template('horario/asistenciaEstudiantes.html', horario = horario, taller = taller, alumnos = alumnos, permisos=permisos, id_horario=id_horario)

def guardarAsistencia():
    User.db = get_db() 
    permisos = User.misPermisos(session['id'])
    data = request.form
    # raise ValueError(data)
    Horario.db=get_db()
    Horario.addAsistencia(data)

    return redirect(url_for('horario_index'))




def delete():
    if not authenticated(session):
        abort(401)  
    User.db = get_db()

    id_user= request.args.get('id')
    permisos = User.misPermisos(session['id'])
    pag= request.args.get('pagina')

    id_horario= request.args.get('id')

    Configuracion.db = get_db()
    config = Configuracion.all()
    Horario.db = get_db()
    Horario.delete(id_horario,pag,config['paginacion'])
    horarios=Horario.all()
    return redirect(url_for('horario_index'))   

def estudiantes_horario():
    if not authenticated(session):
        abort(401)
    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    Horario.db=get_db()
    Estudiante.db=get_db()
    estudiantes=Estudiante.allEstudiantes()
    Horario.db = get_db()
    horarios=Horario.all()
    return render_template('horario/asignarAlumnosHorario.html',estudiantes=estudiantes, horarios=horarios, permisos=permisos)

def add_docentes_horario():
    if not authenticated(session):
        abort(401)
    data = request.form
    Horario.db=get_db()
    Horario.addDocentes(data)
    # raise ValueError(3)
    return redirect(url_for('horario_docentes'))

def docentes_horario():
    if not authenticated(session):
        abort(401)
    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    User.db=get_db()
    Horario.db=get_db()
    docentes=User.docentes()
    horarios=Horario.all()
    return render_template('horario/asignarDocentesHorario.html',docentes=docentes, horarios=horarios, permisos = permisos)

def add_estudiantes_horario():
    if not authenticated(session):
        abort(401)
    data = request.form
    # raise ValueError(data)
    Horario.db=get_db()
    Horario.addEstudiantes(data)
    return redirect(url_for('horario_estudiantes'))

def docentes_asignados():
    if not authenticated(session):
        abort(401)
    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    id_horario = request.args.get('id')
    Horario.db=get_db()
    docentes=Horario.docentes_asignados(id_horario)
    return render_template('horario/docentesAsignados.html',docentes=docentes, id_horario=id_horario, permisos=permisos)


def estudiantes_asignados():
    if not authenticated(session):
        abort(401)
    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    id_horario = request.args.get('id')
    Horario.db=get_db()
    alumnos=Horario.alumnos_asignados(id_horario)
    return render_template('horario/alumnosAsignados.html',alumnos=alumnos, id_horario=id_horario, permisos=permisos)

def update():

    User.db = get_db()
    permisos = User.misPermisos(session['id'])

    id_horario= request.args.get('id')
        
    Ciclo_lectivo_taller.db = get_db()
    ciclos_talleres = Ciclo_lectivo_taller.all()

    Nucleo.db = get_db()
    nucleos = Nucleo.all()

    Dia.db = get_db()
    dias = Dia.all()

    Horario.db = get_db()
    horario = Horario.searchHorario(id_horario)

    return render_template('horario/update.html', permisos = permisos, nucleos = nucleos, dias= dias, ciclos_talleres= ciclos_talleres, horario =horario)


def modificar():
    if not authenticated(session):
        abort(401)

    User.db = get_db()
    permisos = User.misPermisos(session['id'])
    data = request.form
    id_horario = request.args.get('id')
    Ciclo_lectivo_taller.db = get_db()
    ciclos_talleres = Ciclo_lectivo_taller.all()

    Nucleo.db = get_db()
    nucleos = Nucleo.all()

    Dia.db = get_db()
    dias = Dia.all()

    Horario.db = get_db()
    other = Horario.update(data,id_horario)

    return redirect(url_for('horario_index'))
