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

    def _edit(self, word):
        return editor.edit(word)
