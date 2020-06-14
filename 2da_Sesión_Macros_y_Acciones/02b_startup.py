# Archivo startup.py
# Fuente: https://gis.stackexchange.com/a/132714/4972

import qgis
from console import console

def abrir_consola():
    if not console._console:
        # Initialize the console (QGIS knows how)
        qgis.utils.iface.actionShowPythonDialog().trigger()
    console._console.setVisible(True)

qgis.utils.iface.initializationCompleted.connect(abrir_consola)
