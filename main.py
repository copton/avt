import database
from data_model import *

database.setup()

Word(contents=u"hallo", translation=Translation(contents="walk this way"))

