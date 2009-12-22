from menu import Menu, Option
import database
from word import Word as ui_Word

class UI(object):
    def play(self, menu):
        """render the menu and return the choice.

        menu is a ui.Menu object."""
        raise NotImplementedError()

    def textinput(self, prompt):
        """output the prompt and read and return input from the user"""
        raise NotImplementedError()

    def textoutput(self, text):
        """output text"""
        raise NotImplementedError()

    def erroroutput(self, text):
        """output error text and wait for confirmation"""
        raise NotImplementedError()

    def edit(self, db_word):
        """let the user edit the given word, which is a ui.Word object"""
        ui_word = ui_Word(db_word)
        self._edit(ui_word)
        ui_word.update()
        return ui_word.word

    def _edit(self, ui_word):
        raise NotImplementedError()
