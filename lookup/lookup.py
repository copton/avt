import database
from data_model import *
import sys
from ui import Menu, Option, create
from functools import partial

database.setup()
ui = create()

def workflow():
    word = get_search_term()
    for f in [search_in_local_database, search_in_dictionary]:
        found = f(word)
        if found:
            return

def get_search_term():
    if len(sys.argv) != 2:
        sys.stderr.write("usage: %s word\n" % sys.argv[0])
        sys.exit(1)
    return unicode(sys.argv[1])

def search_in_local_database(word):
    words = Word.query.filter(Word.contents.like(u"%%%s" % sys.argv[1])).all()
    if words == []:
        return False

    choice = [-1]

    def select(index):
        choice[0] = index 
        return True

    def menu():
        m = Menu("is it one of these?", delim='\n', footer='\n')
        for i,w in enumerate(words):
            m.addOption(Option("%s: %s" % (w.contents, w.translation.contents), str(i), partial(select, i)))
        return m
                    
    ui.play(menu)

    sys.stdout.write("choice = %d\n" % choice[0])
    return False

def search_in_dictionary(word):
    pass
