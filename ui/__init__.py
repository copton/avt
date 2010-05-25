from menu import Menu, Option
import database

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

    def show(self, word):
        """output word"""
        raise NotImplementedError()

    def edit(self, word):
        """let the user edit the given word"""
