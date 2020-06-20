import os

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUi


class MiDialogo(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        loadUi(os.path.join(os.path.dirname(__file__), "dialogo.ui"), self)

        self.mi_boton.clicked.connect(self.accion)
        self.accepted.connect(self.aceptado)
        self.rejected.connect(self.rechazado)

    def accion(self):
        """ SLOT: acción que realiza el botón cuando se le hace clic """
        self.iface.messageBar().pushInfo("Mi plugin", "Esta es la acción del botón central...")

    def aceptado(self):
        self.iface.messageBar().pushSuccess("Mi plugin", "¡Aceptaste el diálogo!")

    def rechazado(self):
        self.iface.messageBar().pushWarning("Mi plugin", "¡Rechazaste el diálogo!")
