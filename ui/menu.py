class Option(object):
    __slots__=['text', 'key', 'value']

    def __init__(self, text, key, value):
        self.text = text
        assert key.islower() or key.isdigit(), "keys must be lower case or digit"
        self.key = key
        self.value = value

class Menu(object):
    class Quit(object):
        pass
    quit = Quit()

    def __init__(self, header, options=(), quit=True, delim=', ', footer=": ", default=None, confirm=False):
        self.header = header 
        self.default = None
        self.delim = delim
        self.footer = footer
        self.confirm = confirm
        self.options = []
        self.keys = {}
        for text, key, value in options:
            self.addOption(Option(text, key, value))
        if quit:
            self.addQuitOption()
        if default:
            self.setDefault(default)

    def setDefault(self, key):
        assert not self.default, "default flag already set for differnt option"
        assert key in self.keys, "default flag does not exist as key"
        self.default = key

    def addOption(self, option):
        assert not self.keys.has_key(option.key), "key already exists for different option"
        self.keys[option.key] = option
        self.options.append(option)

    def addQuitOption(self):
        self.addOption(Option("quit", "q", Menu.quit))

