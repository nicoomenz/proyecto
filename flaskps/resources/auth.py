from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.configuracion import Configuracion
from flaskps.models.user import User


def login():
    return render_template('auth/login.html')

def home():
    return render_template('home.html')

def authenticate():

    params = request.form
    User.db = get_db()
    user = User.find_by_email_and_pass(params['email'], params['password'])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for('auth_login'))

    session['user'] = user['email']
    session['id'] = user['id']
    permisos = User.misPermisos(user['id'])

    


    Configuracion.db = get_db()
    configuracion= Configuracion.all()
    return render_template('home/index.html', configuracion=configuracion, permisos = permisos)
    # return redirect(url_for('home_index')) #issue_index

def logout():
    del session['user']
    Configuracion.db = get_db()
    configuracion= Configuracion.all()
    return render_template('home/index.html', configuracion=configuracion)
    #return redirect(url_for('auth_login'))
