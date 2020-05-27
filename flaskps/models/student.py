import math

class Estudiante(object):

    db = None

    @classmethod
    def all(cls, pag,config):
        # raise ValueError(int(pag))
        sql = 'SELECT * FROM estudiante AS e WHERE e.eliminado = 0 LIMIT %s,%s '
        cantidad_estudiantes="SELECT COUNT(*) as num_rows FROM estudiate"
        
        cursor = cls.db.cursor()
        cursor.execute(sql,(config*int(pag),config))

        return cursor.fetchall()

    @classmethod
    def allEstudiantes(cls):
        sql = 'SELECT * FROM estudiante'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def rangoAll(cls, config):
        sql="SELECT COUNT(*) as num_rows FROM estudiante"


        cursor = cls.db.cursor()
        cursor.execute(sql)

        num=cursor.fetchall() 
        # raise ValueError(num[0]['num_rows'])       
        numero = int(num[0]['num_rows'])
        con = int(config)

        return math.ceil(numero/con)

    @classmethod
    def create(cls, data):
        tipo_doc_id = data['tipo_doc']
        numero_doc = data['numero_doc']
        nombre=data['first_name']
        apellido=data['last_name']
        nivel_id = data['nivel']
        lugar_nacimiento = data['lugar_de_nacimiento']
        domicilio = data['domicilio']
        localidad = data['localidad']
        escuela = data['escuela']
        fecha_nacimiento = data['fecha_nac']
        telefono = data['telefono']
        barrio_id = data['barrio']
        genero = data['genero']
        responsable = data['responsable']
        estado=data['estado']
        # raise ValueError(genero)

        sql = """
            INSERT INTO estudiante (tipo_doc_id, numero_doc, nombre, apellido, lugar_nacimiento, domicilio, localidad_id, escuela_id, fecha_nac, telefono, barrio_id, estado, eliminado)
            VALUES (%s, %s,%s, %s, %s,%s, %s,%s,%s,%s,%s,%s,%s)
        """


        cursor = cls.db.cursor()
        #---- sql agrega el usuario en la tabla usuario

        cursor.execute(sql, (tipo_doc_id, numero_doc, nombre, apellido, lugar_nacimiento, domicilio, localidad, escuela, fecha_nacimiento, telefono,barrio_id, estado,0))


        #---- sql2 me traigo el ultimo id, del ultimo usuario agregado:
        sql2 = """ SELECT DISTINCT e.id, LAST_INSERT_ID() from estudiante e WHERE e.id = LAST_INSERT_ID() """
        cursor.execute(sql2)
        idEstudiantefetch = cursor.fetchall()
        for i in idEstudiantefetch:
            id_estudiante = (i["id"])

        #---- sql3 tomo el id del genero, a partir del nombre del genero

        sql3 = """SELECT genero.id FROM genero where genero.nombre = %s"""
        id_g = cursor.execute(sql3, (genero))

        id_generofetch = cursor.fetchall()
        for g in id_generofetch:
            id_genero=(g["id"])

        #----- sql4 inserto el id con genero correspondiente en la tabla de usuario_con_genero
        sql4 = """
            INSERT INTO estudiante_con_genero (id_estudiante,id_genero)
            VALUES (%s,%s)
        """    
        cursor.execute(sql4, (id_estudiante,genero))


         #----- sql5 inserto el id con responsable correspondiente en la tabla de usuario_con_responsable
        sql5 = """
            INSERT INTO estudiante_con_responsable (id_estudiante,id_responsable)
            VALUES (%s,%s)
        """    
        cursor.execute(sql5, (id_estudiante,responsable))

        sql6 = """
            INSERT INTO estudiante_con_nivel (id_estudiante,id_nivel)
            VALUES (%s,%s)
        """    
        cursor.execute(sql6, (id_estudiante,nivel_id))

        # cursor.execute(sql,(config*int(pag),config))
        cls.db.commit()


        cls.db.commit()

        return True

    @classmethod
    def modificar(cls,data,pag,config):
        idEstudiante= data['idEstudiante']
        tipo_doc_id = data['tipo_doc']
        numero_doc = data['numero_doc']
        nombre=data['first_name']
        apellido=data['last_name']
        nivel_id = data['nivel']
        lugar_nacimiento = data['lugar_de_nacimiento']
        domicilio = data['domicilio']
        localidad = data['localidad']
        escuela = data['escuela']
        fecha_nacimiento = data['fecha_nac']
        telefono = data['telefono']
        barrio_id = data['barrio']
        genero = data['genero']
        responsable = data['responsable']
        estado=data['estado']

        sql = """
            UPDATE estudiante AS e
            SET e.tipo_doc_id=%s, e.numero_doc=%s, e.nombre=%s, e.apellido=%s, e.lugar_nacimiento=%s, e.domicilio=%s, e.localidad_id=%s, e.escuela_id=%s, e.fecha_nac=%s, e.telefono=%s, e.barrio_id=%s, e.estado=%s
            WHERE e.id =%s
        """

        # raise ValueError(email,password,edad,first_name,last_name,estado)

        
        cursor = cls.db.cursor()
        # raise ValueError(idEstudiante)
        cursor.execute(sql, (tipo_doc_id, numero_doc, nombre, apellido, lugar_nacimiento, domicilio, localidad, escuela, fecha_nacimiento, telefono,barrio_id, estado,idEstudiante))
        
        sql2 = """
                UPDATE estudiante_con_genero as g
                SET g.id_genero = %s
                WHERE g.id_estudiante=%s
        """
        cursor = cls.db.cursor()
        # raise ValueError(idEstudiante)
        cursor.execute(sql2, (genero,idEstudiante))

        sql3 = """
                UPDATE estudiante_con_responsable as ecr
                SET ecr.id_responsable = %s
                WHERE ecr.id_estudiante=%s
        """
        cursor = cls.db.cursor()
        # raise ValueError(idEstudiante)
        cursor.execute(sql3, (responsable,idEstudiante))

        sql4 = """
                UPDATE estudiante_con_nivel as n
                SET n.id_nivel = %s
                WHERE n.id_estudiante=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql4, (nivel_id,idEstudiante))

        # cursor.execute(sql,(config*int(pag),config))
        cls.db.commit()

        return True
   

    @classmethod
    def search(cls, id_e):
        #raise ValueError(id)
        id_u=id_e
        sql="""SELECT * FROM estudiante AS e WHERE e.id = %s"""

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def find_by_documento(cls, documento):
        sql = """
            SELECT * FROM estudiante AS u
            WHERE u.numero_doc = %s 
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, documento)

        return cursor.fetchone()


    @classmethod
    def  delete(cls,id_s,pag,config):
        id_student=id_s
        uno=1
        sql="""UPDATE estudiante AS e SET e.eliminado = %s WHERE e.id = %s"""
        # sql="""SELECT * FROM usuario AS u WHERE u.id = %s"""
        # sql="DELETE FROM usuario WHERE usuario.id = %s"
        
        cursor = cls.db.cursor()
        cursor.execute(sql,(uno,id_student))

        cls.db.commit()

        return cursor.fetchall()

    @classmethod
    def searchIdGender(cls,id_student):
        #raise ValueError(id)
        id_u=id_student
        sql="SELECT id_genero FROM estudiante_con_genero AS u WHERE u.id_estudiante = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def searchIdNivel(cls,id_student):
        #raise ValueError(id)
        id_u=id_student
        sql="SELECT id_nivel FROM estudiante_con_nivel AS u WHERE u.id_estudiante = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def searchIdResponsable(cls,id_student):
        #raise ValueError(id)
        id_u=id_student
        sql="SELECT id_responsable FROM estudiante_con_responsable AS u WHERE u.id_estudiante = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def obtenerResponsables(cls):
        #raise ValueError(id)
        sql="SELECT * FROM responsable"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def obtenerEscuelas(cls):
        #raise ValueError(id)
        sql="SELECT * FROM escuela"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def obtenerBarrios(cls):
        #raise ValueError(id)
        sql="SELECT * FROM barrio"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()


    @classmethod
    def misPermisos(cls, idUser):
        #--- id del rol de mi usuario logueado
        # idRol ="""SELECT id_rol FROM usuario_con_rol ur WHERE ur.id_usuario = %s """ 

        # sql = """ SELECT id_permiso FROM rol_con_permiso rcp WHERE EXISTS (SELECT id_rol FROM usuario_con_rol ur WHERE ur.id_usuario = %s)  """

        sql = """ SELECT nombre FROM permiso p WHERE id IN (SELECT id_permiso FROM rol_con_permiso rcp WHERE id_rol IN (SELECT id_rol FROM usuario_con_rol ur WHERE ur.id_usuario = %s)) """

        cursor = cls.db.cursor()
        cursor.execute(sql, (idUser))
        cls.db.commit()

        return cursor.fetchall()