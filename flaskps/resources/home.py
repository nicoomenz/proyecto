from flask import redirect, render_template, request, url_for, session, abort
from flaskps.db import get_db
from flaskps.models.configuracion import Configuracion
from flaskps.models.home import Home
from flaskps.helpers.auth import authenticated
from flaskps.models.user import User

def index():
	# if not authenticated(session):
	# 	abort(401)
	# raise ValueError(Configuracion.estado())


	User.db = get_db()
	#permisos = User.misPermisos(session['id'])

	Configuracion.db = get_db()
	configuracion = Configuracion.all()
	estado=Configuracion.estado()
	if estado['estado']==0:
		# print("No se puede entrar")
		return render_template('configuracion/error.html')

	return render_template('home/index.html', configuracion=configuracion)

def indexIniciada():
	# if not authenticated(session):
	# 	abort(401)
	# raise ValueError(Configuracion.estado())


	User.db = get_db()
	permisos = User.misPermisos(session['id'])

	Configuracion.db = get_db()
	configuracion = Configuracion.all()
	estado=Configuracion.estado()
	if estado['estado']==0:
		# print("No se puede entrar")
		return render_template('configuracion/error.html')

	return render_template('home/index.html', configuracion=configuracion, permisos=permisos)
