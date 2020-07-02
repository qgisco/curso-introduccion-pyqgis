# Archivo startup.py
# Fuente: https://gis.stackexchange.com/a/358580/4972

from qgis.utils import iface
from console import console

if not console._console:
    # We need to initialize the console (QGIS knows how)
    # and respect the opened/closed state from last session
    iface.actionShowPythonDialog().trigger()
    console._console.setVisible(console._console.isUserVisible())

console._console.console.shell.runcode("""
l = None
def clc(layer):
    global l
    l = layer
iface.currentLayerChanged.connect(clc)
""")
console._console.console.shellOut.clearConsole()
