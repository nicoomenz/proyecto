class Configuracion(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM configuracion'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()

    @classmethod
    def modificar(cls, data):

        titulo = data['titulo']
        descripcion = data['descripcion']
        mail = data['mail']
        estado = data['estado']
        paginacion = data['paginacion']

        sql = """
            UPDATE configuracion AS c
            SET c.titulo= %s, c.descripcion= %s, c.mail = %s, c.estado= %s, c.paginacion= %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (titulo,descripcion,mail,estado,paginacion))
        cls.db.commit()

        return True
    
    @classmethod
    def estado(cls):
        sql='SELECT configuracion.estado FROM configuracion'
        cursor=cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()