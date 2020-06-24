import os.path
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .dialog import SpatialJoinDialog

class SpatialJoin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon(os.path.dirname(os.path.realpath(__file__)) + "/icon.png"), 
                              "Open Spatial Join", 
                              self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        dlg = SpatialJoinDialog(self.iface)
        dlg.exec_()
