import sys

def input(prompt):
    if prompt:
        output(prompt + ": ", newline=False)
    text = sys.stdin.readline().strip()
    return text
    
def output(text, newline=True):
    sys.stdout.write(text)
    if newline:
        sys.stdout.write("\n")
    else:
        sys.stdout.flush()
 
def error(text):
    output(text)
    sys.stdin.readline()
