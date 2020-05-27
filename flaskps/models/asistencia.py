import math

class Asistencia(object):
	
	db = None

	@classmethod
	def show(cls, pag,config):

		sql="""SELECT * FROM asistencias a INNER JOIN estudiante_horario eh 
		ON (a.estudiante_horario = eh.id) INNER JOIN estudiante e ON (e.id = eh.estudiante_id)
		LIMIT %s,%s"""
		cursor = cls.db.cursor()
		cursor.execute(sql,(config*int(pag),config))
		return cursor.fetchall()

	@classmethod
	def rangoAll(cls, config):
	    sql="SELECT COUNT(*) as num_rows FROM asistencias "
	    cursor = cls.db.cursor()
	    cursor.execute(sql)
	    num=cursor.fetchall()
	    numero = int(num[0]['num_rows'])
	    con = int(config)
	    return math.ceil(numero/con)