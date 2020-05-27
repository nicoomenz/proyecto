from flask import redirect, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.configuracion import Configuracion
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User

def index():
	if not authenticated(session):
		abort(401)

	User.db = get_db()
	permisos = User.misPermisos(session['id'])

	Configuracion.db = get_db()
	configuracion = Configuracion.all()
	# raise ValueError(Configuracion.estado())
	# raise ValueError(estado['estado'])
		
	return render_template('configuracion/index.html', configuracion=configuracion, permisos=permisos)

def modificar():
	# if not authenticated(session):
	# 	abort(401)

	User.db = get_db()
	permisos = User.misPermisos(session['id'])

	Configuracion.db = get_db()
	Configuracion.modificar(request.form)
	configuracion = Configuracion.all()
	return render_template('home/index.html', configuracion=configuracion, permisos=permisos)

