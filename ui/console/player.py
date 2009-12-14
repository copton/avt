from getch import getch
import io

def play(menuFactory):
    while True:
        menu = menuFactory()
        io.output(menu.header + "\n")
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
        io.output(menu.delim.join(choices) + menu.footer)
        choice = getch()
        if choice == '\r' and menu.default:
            action = menu.keys[menu.default].action
        else:
            try:
                action = menu.keys[choice.lower()].action
            except KeyError:
                io.output("invalid choice\n")
                continue
        quit = action()
        if quit:
            break
