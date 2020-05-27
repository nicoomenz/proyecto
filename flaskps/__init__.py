from os import path
from flask import Flask, render_template, g
from flaskps.resources import user
from flaskps.resources import auth
from flaskps.resources import instrumentos
from flaskps.resources import configuracion
from flaskps.resources import home
from flaskps.resources import student
from flaskps.resources import ciclo
from flaskps.resources import taller
from flaskps.resources.api import issue as api_issue
from flaskps.config import Config
from flaskps.resources import horario 
from flaskps.resources import asistencia 

# from flask_httpauth import HTTPDigestAuth


# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(Config)

# Home
app.add_url_rule("/home", 'home_index', home.index)
app.add_url_rule("/home/iniciada", 'home_indexIniciada', home.indexIniciada)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule("/autenticacion",'auth_authenticate', auth.authenticate, methods=['POST'])
# app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
# app.add_url_rule("/autenticacion",'auth_authe', auth.authe, methods=['POST'])


# Instrumentos
app.add_url_rule("/instrumentos", 'instrumentos_index', instrumentos.index, methods=['GET'])
app.add_url_rule("/instrumentos", 'instrumentos_create', instrumentos.create, methods=['POST'])
app.add_url_rule("/instrumentos/new", 'instrumentos_new', instrumentos.new)
app.add_url_rule("/instrumentos/update", 'instrumento_update', instrumentos.update, methods=['GET'])
app.add_url_rule("/instrumentos/modificar", 'instrumento_modificar', instrumentos.modificar, methods=['POST'])
app.add_url_rule("/instrumentos/eliminados", 'instrumento_delete', instrumentos.delete, methods=['GET'])
app.add_url_rule("/instrumentos/encontrados", 'instrumento_find', instrumentos.find, methods=['POST'])
app.add_url_rule("/instrumentos/detalles", 'instrumento_show', instrumentos.detail, methods=['GET'])

# Ciclo lectivo
app.add_url_rule("/ciclo", 'ciclo_index', ciclo.index)
app.add_url_rule("/ciclo/show", 'ciclo_show', ciclo.show)
app.add_url_rule("/ciclo/new", 'ciclo_new', ciclo.new) #hacer el create, el new solo para formulario
app.add_url_rule("/ciclo", 'ciclo_create',ciclo.create, methods=['POST'])
app.add_url_rule("/ciclo/asignar",'ciclo_taller',ciclo.asignar)
app.add_url_rule("/ciclo/update", 'ciclo_update', ciclo.update, methods=['GET'])
app.add_url_rule("/ciclo/modificar", 'ciclo_modificar', ciclo.modificar, methods=['POST'])
app.add_url_rule("/ciclo/add",'ciclo_add',ciclo.add, methods=['POST'])
app.add_url_rule("/ciclo/eliminados",'ciclo_delete',ciclo.delete,methods=['GET'])
# @app.route("/ciclo/new")
# def ciclo_new():
# 	return render_template('ciclo/new.html')

# Usuarios
app.add_url_rule("/usuarios", 'user_index', user.index, methods=['GET']) # resources del archivo user usa la funcion index
app.add_url_rule("/usuarios", 'user_create', user.create, methods=['GET','POST'])
app.add_url_rule("/activos", 'user_active', user.active, methods=['GET' ,'POST'])
app.add_url_rule("/bloqueados", 'user_bloq', user.bloq, methods=['GET','POST'])
app.add_url_rule("/usuarios/new", 'user_new', user.new, methods=['GET', 'POST'])
app.add_url_rule("/usuarios/show", 'user_show', user.show, methods=['GET'])
app.add_url_rule("/usuarios/update", 'user_update', user.update, methods=['GET'])
app.add_url_rule("/usuarios/modificar", 'user_modificar', user.modificar, methods=['POST'])
app.add_url_rule("/usuario/encontrado", 'user_find', user.find, methods=['GET','POST'])
app.add_url_rule("/usuarios/eliminados", 'user_delete', user.delete, methods=['GET'])


# Estudiantes
app.add_url_rule("/student", 'student_index', student.index, methods=['GET'])
app.add_url_rule("/student/new", 'student_new', student.new, methods=['GET','POST'])
app.add_url_rule("/student/show", 'student_show', student.show, methods=['GET'])
app.add_url_rule("/student/create", 'student_create', student.create, methods=['GET','POST'])
app.add_url_rule("/student/update", 'student_update', student.update, methods=['GET'])
app.add_url_rule("/student/modificar", 'student_modificar', student.modificar, methods=['POST'])
app.add_url_rule("/student/eliminados", 'student_delete', student.delete, methods=['GET'])

# Talleres
app.add_url_rule("/taller", 'taller_index', taller.index)
app.add_url_rule("/taller/ciclo", 'taller_ciclo', taller.tallerConCiclo)
app.add_url_rule("/taller/show", 'taller_show', taller.show, methods=['GET'])

# Horarios
app.add_url_rule("/horarios", 'horario_index', horario.index)
app.add_url_rule("/horarios/new", 'horario_new', horario.new)
app.add_url_rule("/horarios", 'horario_create', horario.create, methods=['GET','POST'])
app.add_url_rule("/horarios/show", 'horario_show', horario.show, methods=['GET'])
app.add_url_rule("/horarios/update", 'horario_update', horario.update, methods=['GET'])
app.add_url_rule("/horario/modificar", 'horario_modificar', horario.modificar, methods=['POST'])
app.add_url_rule("/horarios/eliminado", 'horario_delete', horario.delete, methods=['GET'])
app.add_url_rule("/horarios/docentes/asignados",'horario_docente_asignado',horario.docentes_asignados,methods=['GET'])
app.add_url_rule("/horarios/alumnos/asignados",'horario_alumnos_asignado',horario.estudiantes_asignados,methods=['GET'])
app.add_url_rule("/horarios/asignar/estudiantes/add",'horario_estudiantes_add',horario.add_estudiantes_horario, methods=['GET','POST'])
app.add_url_rule("/horarios/asignar/docentes/add",'horario_docentes_add',horario.add_docentes_horario, methods=['GET','POST'])
app.add_url_rule("/horarios/asignar/estudiantes",'horario_estudiantes',horario.estudiantes_horario, methods=['GET','POST'])
app.add_url_rule("/horarios/asignar/docentes",'horario_docentes',horario.docentes_horario, methods=['GET','POST'])
app.add_url_rule("/horarios/asistenciaEstudiantes", 'horario_asistencia_index', horario.asistencia, methods=['GET','POST'])
app.add_url_rule("/horarios/guardarAsistencia", 'horario_guardar_asistencia', horario.guardarAsistencia, methods=['GET','POST'])

# Configuracion
app.add_url_rule("/configuracion", 'configuracion_index', configuracion.index)
app.add_url_rule("/configuracion/modificar", 'configuracion_modificar', configuracion.modificar, methods=['POST'])

# Asistencia
app.add_url_rule("/asistencia/show", 'asistencia_show', asistencia.show,methods=['GET','POST'])

# Docentes
app.add_url_rule("/usuarios/docentes", 'docentes_index', user.docentes, methods=['GET','POST'])

# API-rest
app.add_url_rule("/api/consultas", 'api_issue_index', api_issue.index)

app.add_url_rule("/", 'home_index', home.index)



#@app.route("/")
#def home():
#    return render_template(url_for('home_index'))

#app.add_url_rule("/usuarios/new",    'user_new'      , user.new)
						#ruta		alias para python   funcion a ejecutar (en general controler de la carpeta resources)
#del resources voy a models 
