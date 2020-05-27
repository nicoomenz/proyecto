class Ciclo(object):
	
	db = None

	@classmethod
	def all(cls):
		sql = " SELECT * FROM ciclo_lectivo cl WHERE cl.eliminado=0"
		cursor = cls.db.cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@classmethod
	def new(cls):
		# raise ValueError(data)
		return True

	@classmethod
	def create(cls,data):
		# raise ValueError(data)
		semestre=data['semestre']
		fecha_ini=data['fecha_ini']
		fecha_fin=data['fecha_fin']
		sql = """
            INSERT INTO ciclo_lectivo (fecha_ini, fecha_fin, semestre, eliminado)
            VALUES (%s,%s,%s)
        """
		cursor = cls.db.cursor()
		cursor.execute(sql, (fecha_ini, fecha_fin, semestre, 0))
		cls.db.commit()

		return True

	@classmethod
	def searchCiclo(cls, id_ciclo):
		sql = """
			SELECT * FROM ciclo_lectivo WHERE id = %s
		"""
		cursor = cls.db.cursor()
		cursor.execute(sql, (id_ciclo))
		cls.db.commit()

		return cursor.fetchone()

	@classmethod
	def searchFechInic(cls, id_ciclo):
		sql = """
			SELECT fecha_ini FROM ciclo_lectivo WHERE id = %s
		"""
		cursor = cls.db.cursor()
		cursor.execute(sql, (id_ciclo))
		cls.db.commit()

		return cursor.fetchone()

	@classmethod
	def searchFechFin(cls, id_ciclo):
		sql = """
			SELECT fecha_fin FROM ciclo_lectivo WHERE id = %s
		"""
		cursor = cls.db.cursor()
		cursor.execute(sql, (id_ciclo))
		cls.db.commit()

		return cursor.fetchone()


	@classmethod
	def agregarTaller(cls,data):
	    cicloLectivo=data['cicloLectivo']
	    taller=data['taller']
	    # raise ValueError(taller)
	    sql = """INSERT INTO ciclo_lectivo_taller(taller_id,ciclo_lectivo_id)VALUES(%s,%s)"""
	    cursor = cls.db.cursor()
	    cursor.execute(sql,(taller,cicloLectivo))
	    cls.db.commit()
	    return True

	@classmethod
	def modificar(cls,data):
		id_ciclo = data['idCiclo']
		fecha_ini = data['fecha_ini']
		fecha_fin =data['fecha_fin']
		semestre =data['semestre']

		sql = """
			UPDATE ciclo_lectivo AS c 
			SET c.fecha_ini =%s, c.fecha_fin =%s, c.semestre=%s
			WHERE c.id =%s
			"""

        # raise ValueError(email,password,edad,first_name,last_name,estado)

		cursor = cls.db.cursor()
        # raise ValueError(idUser)
		cursor.execute(sql, (fecha_ini,fecha_fin,semestre,id_ciclo))

        # cursor.execute(sql,(config*int(pag),config))
		cls.db.commit()

		return True

	@classmethod
	def search(cls, id_c):
        #raise ValueError(id)
		id_ciclo=id_c
		sql="SELECT * FROM ciclo_lectivo AS c WHERE c.id = %s"

		cursor = cls.db.cursor()
		cursor.execute(sql, id_ciclo)

		return cursor.fetchone()

	@classmethod
	def delete(cls,id_c):
		id_ciclo=id_c
		uno=1
		sql="""UPDATE ciclo_lectivo AS cl SET cl.eliminado = %s WHERE cl.id=%s"""
		cursor = cls.db.cursor()
		cursor.execute(sql,(uno,id_ciclo))
		cls.db.commit()
		return True
