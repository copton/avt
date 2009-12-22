import sys

def input(prompt):
    output(prompt + ": ")
    text = sys.stdin.readline().strip()
    return text
    
def output(text):
    sys.stdout.write(text)
    sys.stdout.flush()

def error(text):
    output(text)
    sys.stdin.readline()
