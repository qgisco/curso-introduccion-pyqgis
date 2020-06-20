from qgis.PyQt.QtWidgets import QAction

from .dialogo import MiDialogo


class MiPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction("Abrir diálogo", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        dlg = MiDialogo(self.iface)
        dlg.exec_()

