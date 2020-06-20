from .mi_plugin import MiPlugin

def classFactory(iface):
    return MiPlugin(iface)

