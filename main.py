import database
from data_model import *
import ui

database.setup()

my_ui = ui.create()

t = Translation(contents=u"hallo")
w = Word(contents=u"hello", translation=t)

my_ui.edit(w)
