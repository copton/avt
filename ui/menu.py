class Option(object):
    __slots__=['text', 'key', 'action']

    def __init__(self, text, key, action):
        self.text = text
        assert key.islower() or key.isdigit(), "keys must be lower case or digit"
        self.key = key
        self.action = action

class Menu(object):
    def __init__(self, header, options=(), quit=True, delim=', ', footer=": ", default=None):
        self.header = header 
        self.default = None
        self.delim = delim
        self.footer = footer
        self.options = []
        self.keys = {}
        for text, key, action in options:
            self.addOption(Option(text, key, action))
        if quit:
            self.addQuitOption()
        if default:
            self.setDefault(default)

    def setDefault(self, key):
        assert not self.default, "default flag already set for differnt option"
        self.default = key

    def addOption(self, option):
        assert not self.keys.has_key(option.key), "key already exists for different option"
        self.keys[option.key] = option
        self.options.append(option)

    def addQuitOption(self):
        self.addOption(Option("quit", "q", lambda : True))

