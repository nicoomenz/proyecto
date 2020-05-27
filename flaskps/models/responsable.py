class Responsable(object):

    db = None

    @classmethod
    def all(cls):
        # raise ValueError(int(pag))
        sql = 'SELECT * FROM responsable'
        
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()