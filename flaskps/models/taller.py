class Taller(object):

    db = None

    @classmethod
    def all(cls):
    	sql = 'SELECT * FROM taller'
    	cursor = cls.db.cursor()
    	cursor.execute(sql)
    	return cursor.fetchall()

    @classmethod
    def obtenerConUnId(cls,idCiclo):
    	sql = """SELECT * FROM taller t INNER JOIN ciclo_lectivo_taller clt ON (t.id=clt.taller_id) 
    	INNER JOIN ciclo_lectivo cl ON (cl.id = clt.ciclo_lectivo_id) WHERE cl.id = %s"""
    	cursor = cls.db.cursor()
    	cursor.execute(sql,idCiclo)
    	return cursor.fetchall()

    @classmethod
    def docentes_asignados(cls,id_taller):
        sql = """SELECT * FROM taller t INNER JOIN docente_taller dt ON (t.id=dt.taller_id) 
        INNER JOIN usuario u ON (u.id=dt.usuario_id) WHERE t.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,id_taller)
        return cursor.fetchall()


    @classmethod
    def alumnos_asignados(cls,id_taller):
        sql = """SELECT e.nombre, e.apellido FROM taller t INNER JOIN estudiante_taller et ON (t.id=et.taller_id) 
        INNER JOIN estudiante e ON (e.id=et.estudiante_id) WHERE t.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,id_taller)
        return cursor.fetchall()

    @classmethod
    def searchTaller(cls,id_taller):
        sql = """SELECT * FROM taller t WHERE t.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,id_taller)
        return cursor.fetchone()

