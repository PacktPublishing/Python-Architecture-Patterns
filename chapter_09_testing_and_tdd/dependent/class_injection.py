
# OOP without dependency injection

class settings:
    WRITER_PATH = './'
    MODEL_FILE = 'model.txt'


class Writer:

    def __init__(self):
        self.path = settings.WRITER_PATH

    def write(self, filename, data):
        with open(self.path + filename, 'w') as fp:
            fp.write(data)


class Model:

    def __init__(self, data):
        self.data = data
        self.filename = settings.MODEL_FILE
        self.writer = Writer()

    def save(self):
        self.writer.write(self.filename, self.data)


# OOP with dependency injection

class WriterInjection:

    def __init__(self, path):
        self.path = path

    def write(self, filename, data):
        with open(self.path + filename, 'w') as fp:
            fp.write(data)


class ModelInjection:

    def __init__(self, data, filename, writer):
        self.data = data
        self.filename = filename
        self.writer = writer

    def save(self):
        self.writer.write(self.filename, self.data)
