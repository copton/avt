import sys

def input(promp):
    output(prompt + ": ")
    text = sys.stdin.readline()
    return text
    
def output(text):
    sys.stdout.write(text)
    sys.stdout.flush()
