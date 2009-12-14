import pprint
import tempfile
import subprocess
import os

def get_editor_command():
    for e in ["EDITOR", "VISUAL"]:
        if os.environ.has_key(e):
            return os.environ[e]

    return "/usr/bin/editor"

def edit(word):
    fd, path = tempfile.mkstemp()
    file = os.fdopen(fd, "w")

    file.write(word.translation + "\n\n")
    file.write("\n".join(word.sentences))

    file.close()

    pid = os.fork()
    if pid == 0:
        cmd = get_editor_command()
        os.execl(cmd, cmd, path)
    os.waitpid(pid, 0)
    
    file = open(path, "r")
    word.contents = file.readline().strip()
    file.readline()
    word.sentences = [line.strip() for line in file.readlines()]
    file.close()  
