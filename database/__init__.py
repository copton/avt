from guppy import *

class Database(object):
    connection_string = RequiredFeature("database.connection_string", isInstanceOf(str))

    def connect(self):
        raise NotImplementedError()

    def flush(self):
        raise NotImplementedError()
    
    def Word(self):
        raise NotImplementedError()

    def Translation(self):
        raise NotImplementedError()

    def Sentence(self):
       raise NotImplementedError()
