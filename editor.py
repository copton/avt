import pprint
import tempfile
import subprocess
import os
import data_model

def get_editor_command():
    for e in ["EDITOR", "VISUAL"]:
        if os.environ.has_key(e):
            return os.environ[e]

    return "/usr/bin/editor"

def word_to_repr(word):
    return {
            "contents" : word.contents,
            "translation" : word.translation.contents,
            "sentences" : [s.contents for s in word.sentences],
        }

def repr_to_word(word, repr):
    word.contents = repr["contents"]
    if word.translation.contents != repr["translation"]:
        word.translation.delete()
        word.translation = data_model.Translation(contents=repr["translation"])

    new_sentences = []
    for s in word.sentences:
        if s.contents in repr["sentences"]:
            new_sentences.append(s)
            repr["sentences"].remove(s.contents)
        else:
            s.delete()
    new_sentences += [data_model.Sentence(contents=c) for c in repr["sentences"]]
    word.sentences = new_sentences

def edit(word):
    d = word_to_repr(word)

    fd, path = tempfile.mkstemp()
    file = os.fdopen(fd, "w")
    file.write(pprint.pformat(d))
    file.close()
    print path

    pid = os.fork()
    if pid == 0:
        cmd = get_editor_command()
        os.execl(cmd, cmd, path)
    os.waitpid(pid, 0)
    
    file = open(path, "r")
    d = eval(file.read())
    file.close()  

    repr_to_word(word, d)
