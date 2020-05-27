class Docente_taller(object):
	
	db = None

	@classmethod
	def add(cls,data):
		# raise ValueError(data)
		c=1

		a=data
		b=data
		# raise ValueError(a.getlist('docente'))
		a=a.getlist('docente')
		b=b.getlist('taller')
		# raise ValueError(a)
		sql="""INSERT INTO docente_taller(taller_id, usuario_id) VALUES  (%s,%s)"""


		for i in a:
			# raise ValueError(i)
			cursor = cls.db.cursor()
			cursor.execute(sql,(b,i))
			cls.db.commit()

		return cursor.fetchall()