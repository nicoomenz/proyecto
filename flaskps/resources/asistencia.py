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
from flaskps.models.asistencia import Asistencia


def show():
	if not authenticated(session):
		abort(401)
	pag= request.args.get('pagina')

	Configuracion.db = get_db()
	config = Configuracion.all()

	# raise ValueError(pag)

	# User.db = get_db()
	# users = User.all(page,config['paginacion'])

	
	User.db = get_db()
	permisos = User.misPermisos(session['id'])

	Asistencia.db=get_db()
	rango = Asistencia.rangoAll(config['paginacion'])

	asistencias = Asistencia.show(pag, config['paginacion'])

	return render_template('asistencia/show.html', asistencias=asistencias,pages=config['paginacion'],rango=rango,vista='asistencia_show',permisos=permisos)