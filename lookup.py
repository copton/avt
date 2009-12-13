import database
from data_model import *
import sys
import editor

database.setup()


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
    if words:
        editor.edit(words[0])            

def search_in_dictionary(word):
    pass

workflow()
