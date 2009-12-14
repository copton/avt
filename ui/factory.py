import config

def create():
    module_name = "ui." + config.ui_type
    ui_module = __import__(module_name, {}, {}, module_name)
    return ui_module.UI()
