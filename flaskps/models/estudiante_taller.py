class Estudiante_taller(object):
	
	db = None

	@classmethod
	def add(cls,data):
		# raise ValueError(data)
		id_alumno=data['alumno']
		id_taller=data['taller']
		sql="""INSERT INTO estudiante_taller(estudiante_id, taller_id) VALUES (%s,%s)"""
		cursor = cls.db.cursor()
		cursor.execute(sql,(id_alumno,id_taller))
		cls.db.commit()
		return cursor.fetchall()