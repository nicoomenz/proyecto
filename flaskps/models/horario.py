class Horario(object):

    db = None
    @classmethod
    def all(cls):
        sql = """SELECT * 
        FROM horario h INNER JOIN nucleo n ON h.nucleo = n.id INNER JOIN 
        ciclo_lectivo_taller clt ON clt.id = h.ciclo_lectivo_taller INNER JOIN
        ciclo_lectivo cl ON cl.id = clt.ciclo_lectivo_id INNER JOIN 
        taller t ON clt.taller_id = t.id WHERE h.eliminado = 0
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        ciclo_taller=data['ciclo_taller']
        nucleo=data['nucleo']
        dia_id=data['dia']
        hora_ini=data['hora_ini']
        hora_fin=data['hora_fin']

        sql = """
            INSERT INTO horario (ciclo_lectivo_taller, nucleo, dia_id, hora_ini, hora_fin, eliminado)
            VALUES (%s, %s,%s, %s, %s,%s)
        """

        cursor = cls.db.cursor()
        #---- sql agrega el usuario en la tabla usuario

        cursor.execute(sql, (ciclo_taller, nucleo, dia_id, hora_ini, hora_fin,0))

        cls.db.commit()

        return True

    @classmethod
    def searchHorario(cls,id_horario):
        sql = """SELECT * FROM horario h 
        INNER JOIN ciclo_lectivo_taller clt ON clt.id = h.ciclo_lectivo_taller 
        INNER JOIN ciclo_lectivo cl ON clt.ciclo_lectivo_id = cl.id 
        INNER JOIN taller t ON clt.taller_id = t.id WHERE h.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql, (id_horario))
        return cursor.fetchone()

    @classmethod
    def searchHorariosTaller(cls,id_taller):
        sql = """SELECT * FROM horario h 
        INNER JOIN ciclo_lectivo_taller clt ON clt.id = h.ciclo_lectivo_taller 
        INNER JOIN ciclo_lectivo cl ON clt.ciclo_lectivo_id = cl.id 
        INNER JOIN taller t ON clt.taller_id = t.id WHERE t.id=%s AND h.eliminado = 0"""

        cursor = cls.db.cursor()
        cursor.execute(sql,id_taller)
        return cursor.fetchall()

    @classmethod
    def delete(cls,id_horario,pag,config):
        id_horario=id_horario
        uno=1
        sql="""UPDATE horario AS h SET h.eliminado = %s WHERE h.id = %s"""
        # sql="""SELECT * FROM usuario AS u WHERE u.id = %s"""
        # sql="DELETE FROM usuario WHERE usuario.id = %s"
        
        cursor = cls.db.cursor()
        cursor.execute(sql,(uno,id_horario))

        cls.db.commit()

        return cursor.fetchall()

    @classmethod
    def docentes_asignados(cls,id_horario):
        sql = """SELECT * FROM horario h INNER JOIN docente_horario dh ON (h.id=dh.horario_id) 
        INNER JOIN usuario u ON (u.id=dh.usuario_id) WHERE h.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,id_horario)
        return cursor.fetchall()


    @classmethod
    def alumnos_asignados(cls,id_horario):
        sql = """SELECT e.id, e.nombre, e.apellido, e.numero_doc FROM horario h INNER JOIN estudiante_horario eh ON (h.id=eh.horario_id) 
        INNER JOIN estudiante e ON (e.id=eh.estudiante_id) WHERE h.id=%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,(id_horario))
        return cursor.fetchall()

    @classmethod
    def addEstudiantes(cls,data):
        # raise ValueError(data)
        c=1

        a=data
        b=data
        # raise ValueError(a.getlist('docente'))
        a=a.getlist('estudiante')
        b=b.getlist('horario')
        # raise ValueError(a)
        sql="""INSERT INTO estudiante_horario(horario_id, estudiante_id) VALUES  (%s,%s)"""


        for i in a:
            # raise ValueError(i)
            cursor = cls.db.cursor()
            cursor.execute(sql,(b,i))
            cls.db.commit()

        return cursor.fetchall()

    @classmethod
    def addDocentes(cls,data):
        # raise ValueError(data)
        c=1

        a=data
        b=data
        # raise ValueError(a.getlist('docente'))
        a=a.getlist('docente')
        b=b.getlist('horario')
        # raise ValueError(a)
        sql="""INSERT INTO docente_horario(horario_id, usuario_id) VALUES  (%s,%s)"""


        for i in a:
            # raise ValueError(i)
            cursor = cls.db.cursor()
            cursor.execute(sql,(b,i))
            cls.db.commit()

        return cursor.fetchall()

    @classmethod #Se pone el presente
    def addAsistencia(cls,data):
        # raise ValueError(data)

        a=data
        b=data
        # raise ValueError(a)
        #raise ValueError(fecha)
        a=a.getlist('checkAsistencia')
        b=b.getlist('fecha_asist')
        # raise ValueError(a)
        sql="""SELECT id FROM estudiante_horario WHERE estudiante_id = %s """

        sql2="""INSERT INTO asistencias(estudiante_horario, asistencia, fecha) VALUES  (%s,%s,%s)"""




        for i in a:
            # raise ValueError(i)
            cursor = cls.db.cursor()
            cursor.execute(sql,(i))
            cursor.execute(sql2,(i,1,b))
            cls.db.commit()

        return cursor.fetchall()

    def select_horario_repetido(cls,data):
        ciclo_taller = data['ciclo_taller']
        nucleo = data['nucleo']
        dia=data['dia']
        hora_ini=data['hora_ini']
        hora_fin = data['hora_ini']

        sql = """SELECT * FROM horario WHERE ciclo_lectivo_taller = %s AND nucleo = %s AND dia_id = %s AND hora_ini = %s AND hora_fin = %s"""
        cursor = cls.db.cursor()
        cursor.execute(sql,(ciclo_taller,nucleo,dia,hora_ini,hora_fin))
        cls.db.commit()
        return cursor.fetchall()

    @classmethod
    def searchIdCicloLecTal(cls,id_horario):
        
        sql = """SELECT h.ciclo_lectivo_taller FROM horario h WHERE h.id = %s"""
        cursor = cls.db.cursor()
        cursor.execute(sql,(id_horario))
        cls.db.commit()
        return cursor.fetchone()

    @classmethod
    def update(cls, data, id_horario):
        ciclo_taller=data['ciclo_taller']
        nucleo=data['nucleo']
        dia_id=data['dia']
        hora_ini=data['hora_ini']
        hora_fin=data['hora_fin']
        id_horario = id_horario
        sql = """
            UPDATE horario as h 
            SET h.ciclo_lectivo_taller= %s, h.nucleo= %s, h.dia_id=%s, h.hora_ini= %s, h.hora_fin=%s
            WHERE h.id = %s
        """

        cursor = cls.db.cursor()
        #---- sql agrega el usuario en la tabla usuario

        cursor.execute(sql, (ciclo_taller, nucleo, dia_id, hora_ini, hora_fin, id_horario))

        cls.db.commit()

        return True
