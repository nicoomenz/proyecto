import math

class Instrumento(object):

    db = None

    @classmethod
    def all(cls,pag,config):
        sql = """SELECT i.id, i.nombre, i.descripcionDeEstado, ti.name, i.imagen FROM instrumento i 
        INNER JOIN tipoinstrumento ti ON i.tipoInstrumento_id = ti.id WHERE i.eliminado = 0 
        LIMIT %s,%s"""

        cursor = cls.db.cursor()
        cursor.execute(sql,(config*int(pag),config))

        return cursor.fetchall()

    @classmethod
    def rango(cls, config):
        sql="SELECT COUNT(*) as num_rows FROM instrumento "
        cursor = cls.db.cursor()
        cursor.execute(sql)
        num=cursor.fetchall()
        numero = int(num[0]['num_rows'])
        con = int(config)
        return math.ceil(numero/con)

    @classmethod
    def create(cls, data,imagen):
        nombre=data['nombre']
        descripcionDeEstado=data['descripcionDeEstado']
        tipoInstrumento_id=data['tipoInstrumento_id']
        # imagen=data['imagen']
        sql = """
            INSERT INTO instrumento (nombre, descripcionDeEstado, tipoInstrumento_id, imagen, eliminado)
            VALUES (%s, %s, %s,%s,%s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, descripcionDeEstado, tipoInstrumento_id, imagen, 0))
        cls.db.commit()

        return True

    @classmethod
    def search(cls, id_inst):
        #raise ValueError(id)
        sql="SELECT * FROM instrumento AS i WHERE i.id = %s"

        cursor = cls.db.cursor()
        cursor.execute(sql, id_inst)

        return cursor.fetchone()
   
    @classmethod
    def modificar(cls, data):

        idInstrumento = data['idInstrumento']
        nombre = data['nombre']
        descripcionDeEstado = data['descripcionDeEstado']
        tipoInstrumento_id=data['tipoInstrumento_id']

        sql = """
            UPDATE instrumento AS i
            SET i.nombre= %s, i.descripcionDeEstado= %s, i.tipoInstrumento_id = %s
            WHERE i.id = %s
        """
        # raise ValueError(email,password,edad,first_name,last_name,estado)


        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre,  descripcionDeEstado, tipoInstrumento_id, idInstrumento))
        cls.db.commit()

        return True


    @classmethod
    def delete(cls, id_inst):
        id_i=id_inst
        uno=1
        sql="""UPDATE instrumento AS i SET i.eliminado = %s WHERE i.id = %s"""
        
        cursor = cls.db.cursor()
        cursor.execute(sql, (uno,id_i))
        cls.db.commit()

        return cursor.fetchall()

    @classmethod
    def obtenerId(cls, id_inst):
        sql="""SELECT * FROM instrumento i INNER JOIN tipoinstrumento ti ON (i.tipoInstrumento_id = ti.id) 
        WHERE i.id=%s"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_inst))
        return cursor.fetchone()

    # @classmethod
    # def find(cls, data):
    #     nombre=data['nombre']
    #     sql="SELECT * FROM instrumento AS u WHERE i.nombre = %s "

    #     cursor = cls.db.cursor()
    #     cursor.execute(sql,(nombre,config*int(pag),config))

    #     return cursor.fetchall()

    # @classmethod
    # def rangoFind(cls,data,config):
    #     nombre=data['nombre']

    #     sql="SELECT COUNT(*) as num_rows FROM instrumento WHERE nombre = %s"


    #     cursor = cls.db.cursor()
    #     cursor.execute(sql,nombre)

    #     num=cursor.fetchall() 

    #     numero = int(num[0]['num_rows'])
    #     con = int(config)

    #     return math.ceil(numero/con)

    @classmethod
    def find_by_codigo(cls, codigo):
        sql = """
            SELECT * FROM instrumento AS i
            WHERE i.descripcionDeEstado = %s 
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, codigo)

        return cursor.fetchone()
