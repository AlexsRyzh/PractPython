
class raises:
    def __init__(self, error):
        self.err = error

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if (self.err == type):
            return True
        return False


with raises(ZeroDivisionError) as r:
    10/0
