class Ciclo_lectivo_taller(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT ciclo_lectivo_taller.id, semestre, fecha_ini, fecha_fin, taller.nombre FROM ciclo_lectivo INNER JOIN ciclo_lectivo_taller ON ciclo_lectivo_taller.ciclo_lectivo_id = ciclo_lectivo.id INNER JOIN taller ON ciclo_lectivo_taller.taller_id = taller.id'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def searchCLT(cls,id_clt):
        sql = """SELECT * FROM ciclo_lectivo INNER JOIN 
        ciclo_lectivo_taller ON ciclo_lectivo_taller.ciclo_lectivo_id = ciclo_lectivo.id INNER JOIN
        taller ON ciclo_lectivo_taller.taller_id = taller.id WHERE ciclo_lectivo_taller.id = %s"""
        cursor = cls.db.cursor()
        cursor.execute(sql,id_clt)
        
        return cursor.fetchall()