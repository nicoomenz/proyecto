class Nucleo(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM nucleo'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()