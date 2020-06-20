import os

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUi
from qgis.core import QgsMapLayer

class MiDialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(os.path.join(os.path.dirname(__file__), "dialogo.ui"), self)

        self.mMapLayerComboBox.layerChanged.connect(self.mostrar_resumen)

    def mostrar_resumen(self, layer):
        resumen = "Nombre: {}".format(layer.name())
        crs = "CRS: {}".format(layer.crs().description())

        if layer.type() == QgsMapLayer.VectorLayer:
            conteo = "Número de objetos: {}".format(layer.featureCount())
        elif layer.type() == QgsMapLayer.RasterLayer:
            conteo = "Número de bandas: {}".format(layer.bandCount())

        self.txt_resumen.setText("{}\n{}\n{}".format(resumen, crs, conteo))

