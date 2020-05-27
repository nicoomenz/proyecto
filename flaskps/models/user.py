import math

class User(object):

    db = None

    @classmethod
    def all(cls, pag,config):
        # raise ValueError(int(pag))
        sql = 'SELECT * FROM usuario AS u WHERE u.eliminado = 0 LIMIT %s,%s'
        cantidad_usuario="SELECT COUNT(*) as num_rows FROM usuario WHERE eliminado = 1"
        
        cursor = cls.db.cursor()
        cursor.execute(sql,(config*int(pag),config))

        return cursor.fetchall()

    @classmethod
    def select_user_by_name(cls,name):
        sql = """SELECT * FROM usuario u WHERE u.first_name = %s"""
        cursor = cls.db.cursor()
        cursor.execute(sql,name)

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



    @classmethod
    def create(cls, data):
        email=data['email']
        password=data['password']
        first_name=data['first_name']
        last_name=data['last_name']
        estado=data['estado']
        nombreRol = data['rol']
        fecha_nacimiento = data['fecha_nac']
        tipo_documento = data['tipo_doc']
        num_doc = data['numero_doc']
        domicilio = data['domicilio']
        localidad = data['localidad']
        telefono = data['telefono']
        genero = data['genero']
        # raise ValueError(genero)

        sql = """
            INSERT INTO usuario (tipo_documento, num_doc, email, password, first_name, last_name, estado, domicilio, localidad, fecha_nacimiento, telefono, eliminado)
            VALUES (%s, %s,%s, %s, %s,%s, %s,%s,%s,%s,%s,%s)
        """


        cursor = cls.db.cursor()
        #---- sql agrega el usuario en la tabla usuario

        cursor.execute(sql, (tipo_documento, num_doc, email, password, first_name, last_name, estado, domicilio, localidad, fecha_nacimiento, telefono,0))


        #---- sql2 me traigo el ultimo id, del ultimo usuario agregado:
        sql2 = """ SELECT DISTINCT u.id, LAST_INSERT_ID() from usuario u WHERE u.id = LAST_INSERT_ID() """
        cursor.execute(sql2)
        idUserfetch = cursor.fetchall()
        for i in idUserfetch:
            id_usuario = (i["id"])

        #---- sql3 tomo el id del rol, a partir del nombre del rol
        sql3 = """ SELECT r.id from rol r WHERE r.name = %s """
        cursor.execute(sql3, (nombreRol))
        id_rolfetch = cursor.fetchall()
        for r in id_rolfetch:
            id_rol=(r["id"])

        #----- sql4 inserto el id con rol correspondiente en la tabla de usuario_con_rol
        sql4 = """
            INSERT INTO usuario_con_rol (id_usuario,id_rol)
            VALUES (%s,%s)
        """    
        cursor.execute(sql4, (id_usuario,id_rol))
        
        #---- sql5 me traigo el ultimo id, del ultimo usuario agregado:

        #sql5 = """ SELECT DISTINCT u.id, LAST_INSERT_ID() from usuario u WHERE u.id = LAST_INSERT_ID() """
        #cursor.execute(sql5)

        #idUserfetch = cursor.fetchall()
        #for i in idUserfetch:
        #    id_usuario = (i["id"])

        #---- sql6 tomo el id del genero, a partir del nombre del genero

        sql6 = """SELECT genero.id FROM genero where genero.nombre = %s"""
        id_g = cursor.execute(sql6, (genero))

        id_generofetch = cursor.fetchall()
        for g in id_generofetch:
            id_genero=(g["id"])

        #----- sql7 inserto el id con genero correspondiente en la tabla de usuario_con_genero
        sql7 = """
            INSERT INTO usuario_con_genero (id_usuario,id_genero)
            VALUES (%s,%s)
        """    
        cursor.execute(sql7, (id_usuario,genero))


        cls.db.commit()

        return True

    @classmethod
    def modificar(cls,data,pag,config):
        idUser = data['idUser']
        email=data['email']
        password=data['password']
        first_name=data['first_name']
        last_name=data['last_name']
        estado=data['estado']
        nombreRol = data['rol']
        fecha_nacimiento = data['fecha_nac']
        tipo_documento = data['tipo_doc']
        num_doc = data['numero_doc']
        domicilio = data['domicilio']
        localidad = data['localidad']
        telefono = data['telefono']
        genero = data['genero']

        sql = """
            UPDATE usuario AS u 
            SET u.tipo_documento =%s, u.num_doc =%s, u.email=%s, u.password=%s, u.first_name=%s, u.last_name=%s, u.estado=%s, u.domicilio=%s, u.localidad=%s, u.fecha_nacimiento=%s, u.telefono=%s
            WHERE u.id =%s
        """

        # raise ValueError(email,password,edad,first_name,last_name,estado)

        
        cursor = cls.db.cursor()
        # raise ValueError(idUser)
        cursor.execute(sql, (tipo_documento, num_doc, email, password, first_name, last_name, estado, domicilio, localidad, fecha_nacimiento, telefono,idUser))
        
        sql2 = """
                UPDATE usuario_con_genero as g
                SET g.id_genero = %s
                WHERE g.id_usuario=%s
        """
        cursor = cls.db.cursor()
        # raise ValueError(idUser)
        cursor.execute(sql2, (genero,idUser))

        sql3 = """
                UPDATE usuario_con_rol as r
                SET r.id_rol = %s
                WHERE r.id_usuario=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql3, (nombreRol,idUser))

        # cursor.execute(sql,(config*int(pag),config))
        cls.db.commit()

        return True

    @classmethod
    def active(cls,pag,config):
        sql = """
            SELECT * FROM usuario WHERE estado = 0 and eliminado = 0 LIMIT %s,%s
        """
        cantidad_usuario="SELECT COUNT(*) as num_rows FROM usuario"

        cursor = cls.db.cursor()
        # cursor.execute(sql,(pag,config))
        cursor.execute(sql,(config*int(pag),config))
        return cursor.fetchall()

    @classmethod
    def bloq(cls,pag,config):
        sql = """
            SELECT * FROM usuario WHERE estado = 1 and eliminado = 0 LIMIT %s,%s
        """
        cantidad_usuario="SELECT COUNT(*) as num_rows FROM usuario"


        cursor = cls.db.cursor()
        cursor.execute(sql,(config*int(pag),config))

        return cursor.fetchall()


    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.email = %s AND u.password = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (email, password))

        return cursor.fetchone()

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.email = %s 
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, email)

        return cursor.fetchone()

    @classmethod
    def find_by_documento(cls, documento):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.num_doc = %s 
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, documento)

        return cursor.fetchone()

    @classmethod
    def find(cls, data,pag,config):
        nombre=data['nombre']
        sql="SELECT * FROM usuario AS u WHERE u.email LIKE %s LIMIT %s,%s"

        cursor = cls.db.cursor()
        cursor.execute(sql,(nombre+"%",config*int(pag),config))

        return cursor.fetchall()

    @classmethod
    def search(cls, id_us):
        #raise ValueError(id)
        id_u=id_us
        sql="SELECT * FROM usuario AS u WHERE u.id = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def searchIdGender(cls,id_us):
        #raise ValueError(id)
        id_u=id_us
        sql="SELECT id_genero FROM usuario_con_genero AS u WHERE u.id_usuario = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()

    @classmethod
    def searchIdRol(cls,id_user):
        #raise ValueError(id)
        id_u=id_user
        sql="SELECT name FROM rol WHERE id IN (SELECT id_rol FROM usuario_con_rol AS u WHERE u.id_usuario = %s)"
        cursor = cls.db.cursor()
        cursor.execute(sql, id_u)

        return cursor.fetchone()



    @classmethod
    def delete(cls, id_us,pag,config):
        id_u=id_us
        uno=1
        sql="""UPDATE usuario AS u SET u.eliminado = %s WHERE u.id = %s"""
        # sql="""SELECT * FROM usuario AS u WHERE u.id = %s"""
        # sql="DELETE FROM usuario WHERE usuario.id = %s"
        
        cursor = cls.db.cursor()
        cursor.execute(sql,(uno,id_u))

        cls.db.commit()

        return cursor.fetchall()


    @classmethod
    def rangoAll(cls, config):
        sql="SELECT COUNT(*) as num_rows FROM usuario WHERE eliminado = 0"


        cursor = cls.db.cursor()
        cursor.execute(sql)

        num=cursor.fetchall() 
        # raise ValueError(num[0]['num_rows'])       
        numero = int(num[0]['num_rows'])
        con = int(config)

        return math.ceil(numero/con)


    @classmethod
    def rangoActive(cls, config):
        sql="SELECT COUNT(*) as num_rows FROM usuario as u WHERE u.estado = 0 and eliminado = 0"


        cursor = cls.db.cursor()
        cursor.execute(sql)

        num=cursor.fetchall() 
        
        # raise ValueError(num[0]['num_rows'])       
        numero = int(num[0]['num_rows'])
        con = int(config)

        return math.ceil(numero/con)


    @classmethod
    def rangoBloq(cls, config):
        sql="SELECT COUNT(*) as num_rows FROM usuario as u WHERE u.estado = 1 and eliminado = 0"


        cursor = cls.db.cursor()
        cursor.execute(sql)

        num=cursor.fetchall() 
        
        # raise ValueError(num[0]['num_rows'])       
        numero = int(num[0]['num_rows'])
        con = int(config)

        return math.ceil(numero/con)

    @classmethod
    def rangoFind(cls,data,config):
        
        # if data['nombre']:
        #     nombre=data['nombre']
        # else:
        #     nombre=name

        nombre=data['nombre']

        sql="SELECT COUNT(*) as num_rows FROM usuario WHERE email LIKE %s and eliminado = 0"


        cursor = cls.db.cursor()
        cursor.execute(sql,nombre+"%")

        num=cursor.fetchall() 

        numero = int(num[0]['num_rows'])
        con = int(config)

        return math.ceil(numero/con)


    @classmethod
    def docentes(cls):
        sql="""SELECT * FROM usuario u INNER JOIN usuario_con_rol ucr ON (u.id=ucr.id_usuario) 
        INNER JOIN rol r ON (r.id=ucr.id_rol) WHERE r.id=2"""

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
