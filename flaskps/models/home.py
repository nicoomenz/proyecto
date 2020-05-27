class Home(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM configuracion'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()