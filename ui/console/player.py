from getch import getch
import io

def play(menu):
    while True:
        io.output(menu.header)
        choices = []
        for option in menu.options:
            if option.key == menu.default:
                pkey = option.key.upper()
            else:
                pkey = option.key

            if option.key in option.text:
                choices.append(option.text.replace(option.key, "(%s)" % pkey, 1))
            else:
                choices.append("(%s) %s" % (pkey, option.text))

        io.output(menu.delim.join(choices) + menu.footer, newline=False)

        default = False
        if menu.confirm:
            choice = io.input(None)
            if choice == "":
                default = True
        else:
            choice = getch()
            if choice == '\r':
                default = True

        if default:
            if menu.default:
                value = menu.keys[menu.default].value
            else:
                io.output("invalid choice\n")
        else:
            try:
                value = menu.keys[choice.lower()].value
            except KeyError:
                io.output("invalid choice\n")
                continue

        return value
