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
    if words == []:
        return False

    sys.stdout.write("is it one of these? (0 means 'no')\n")
    for i, word in enumerate(words):
        sys.stdout.write("%d: %s: %s\n" % (i + 1, word.contents, word.translation.contents))
    number = getch()
    print "__" + number + "___"
    if number == '0':
        print "is 0"
        return False
    else:  
        return True
         

def search_in_dictionary(word):
    pass

workflow()
