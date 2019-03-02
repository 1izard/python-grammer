import __main__


class TestingDatabase(object):
    def __init__(self):
        super().__init__()
        print('TestingDatabase : ', self)


class RealDatabase(object):
    def __init__(self):
        super().__init__()
        print('RealDatabase : ', self)


if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase
