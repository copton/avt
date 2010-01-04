import player
import io
import editor
from ui import UI as Base

class UI(Base):
    def play(self, menuFactory):
        return player.play(menuFactory)

    def textinput(self, prompt):
        return io.input(prompt)

    def textoutput(self, text, newline=True):
        return io.output(text, newline)

    def erroroutput(self, text):
        return io.error(text)

    def _edit(self, word):
        return editor.edit(word)
