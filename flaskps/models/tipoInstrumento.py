class TipoInstrumento(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM tipoinstrumento'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()