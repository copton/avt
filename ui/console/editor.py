import tempfile
import os
import io
import re

def get_editor_command():
    for e in ["EDITOR", "VISUAL"]:
        if os.environ.has_key(e):
            return os.environ[e]

    return "/usr/bin/editor"

def parse(file, word):
    marker = re.compile("<([^>]*)>")
    state = 0
    for line in file.readlines():
        line = line.strip()
        print line, state
        if line.startswith("#"):
            continue
        if line == "":
            continue

        if state == 0:
            mo = marker.match(line)
            if mo == None or mo.group(1) != "translation":
                return "missing <translation> marker. Found '%s' instead" % line
            else: 
                state = 1
        elif state == 1:
            mo = marker.search(line)
            if mo:
                return "found marker '%s' but expected translation of word" % mo.group(1)
            else:
                word.translation = line
                state = 2
        elif state == 2:
            mo=marker.match(line)
            if mo == None or mo.group(1) != "sentences":
                return "missing <sentences> marker. Found '%s' instead" % line
            else:
                state = 3
                word.sentences = []
        elif state == 3:
            mo = marker.search(line)
            if mo:
                return "found marker '%s' but expected sentence with word" % mo.group(1)
            else:
                word.sentences.append(line) 

    return None
        
def edit(word):
    fd, path = tempfile.mkstemp()
    file = os.fdopen(fd, "w")

    file.write("# editing '" + word.contents + "'\n")
    file.write("<translation>\n")
    file.write(word.translation + "\n")
    file.write("<sentences>\n")
    file.write("\n".join(word.sentences) + "\n")

    file.close()

    while True:
        pid = os.fork()
        if pid == 0:
            cmd = get_editor_command()
            os.execl(cmd, cmd, path)
        os.waitpid(pid, 0)
    
        file = open(path, "r")
        error = parse(file, word)
        file.close()
        if error == None:
            return
        else:
            io.error("format failure: '%s'. Please fix" % error)    
        
