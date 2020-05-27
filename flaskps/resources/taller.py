from flask import redirect, render_template, request, url_for, session, abort
import requests
import json
from flaskps.db import get_db
from flaskps.models.ciclo import Ciclo
from flaskps.models.estudiante_taller import Estudiante_taller
from flaskps.models.docente_taller import Docente_taller
from flaskps.models.taller import Taller
from flaskps.models.student import Estudiante
from flaskps.models.horario import Horario
from flaskps.models.dia import Dia
from flaskps.models.nucleo import Nucleo
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User


def index():


	User.db = get_db()
	permisos = User.misPermisos(session['id'])


	Taller.db = get_db()
	# id_ciclo = request.args.get('id')
	# talleres = Taller.obtenerConUnId(id_ciclo)
	talleres=Taller.all()
	return render_template('taller/index.html',talleres=talleres, permisos=permisos)


def tallerConCiclo():
	# User.db = get_db()
	permisos = User.misPermisos(session['id'])


	Taller.db = get_db()
	id_ciclo = request.args.get('id')
	talleres = Taller.obtenerConUnId(id_ciclo)

	return render_template('taller/index.html',talleres=talleres, permisos=permisos)

def usuarios_alumnos_talleres():
    if not authenticated(session):
        abort(401)
    permisos = User.misPermisos(session['id'])

    # User.db=get_db()
    Taller.db=get_db()
    Estudiante.db=get_db()
    estudiantes=Estudiante.allEstudiantes()
    # docentes=User.docentes()
    talleres=Taller.all()
    return render_template('taller/asignarAlumnosTaller.html',alumnos=estudiantes, talleres=talleres, permisos=permisos)


def add_alumnos_talleres():
	if not authenticated(session):
		abort(401)

	data = request.form
	# raise ValueError(data)
	Estudiante_taller.db=get_db()
	Estudiante_taller.add(data)
	return redirect(url_for('taller_alumnos'))

def show():
	User.db = get_db() 
	permisos = User.misPermisos(session['id'])
	Taller.db = get_db()
	talleres = Taller.all()
	id_taller = request.args.get('id')
	taller = Taller.searchTaller(id_taller)
	Horario.db = get_db()
	horarios = Horario.searchHorariosTaller(id_taller)
	Dia.db= get_db()
	dias = Dia.all()
	Nucleo.db = get_db()
	nucleos = Nucleo.all()

	return render_template('taller/show.html', horarios= horarios, nucleos = nucleos, dias =dias ,taller=taller, permisos=permisos)

