class Dia(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM dias'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()