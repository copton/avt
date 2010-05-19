import player
import io
import editor
from ui import UI as Base

class UI(Base):
    def play(self, menuFactory):
        return player.play(menuFactory)

    def textinput(self, prompt):
        return io.input(prompt)

    def textoutput(self, text):
        return io.output(text)

    def erroroutput(self, text):
        return io.error(text)

    def show(self, word):
        return io.show(word)

    def _edit(self, word):
        return editor.edit(word)
