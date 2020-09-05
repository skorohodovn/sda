class DB(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.dbEngine = "DDB"

    def connect(self):
        pass
class Page(object):

    def test1(self):
        pass

    def test2(self):
        pass

if __name__ == "__main__":
    db1 = DB()
    db2 = DB()
    db3 = DB()
    print(db1 == db2)