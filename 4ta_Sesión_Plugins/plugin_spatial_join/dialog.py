import os

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUi
from qgis.core import QgsMapLayer, edit, QgsMapLayerProxyModel, QgsFieldProxyModel


class SpatialJoinDialog(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        loadUi(os.path.join(os.path.dirname(__file__), "dialog.ui"), self)
        self.iface = iface
        
        # Only point layers and string fields
        self.cbo_points.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.cbo_target_field.setFilters(QgsFieldProxyModel.String)
        
        # Only polygon layers
        self.cbo_polygons.setFilters(QgsMapLayerProxyModel.PolygonLayer)

        # Initialize field combos
        self.cbo_target_field.setLayer(self.cbo_points.currentLayer())
        self.cbo_source_field.setLayer(self.cbo_polygons.currentLayer())

        # SIGNAL-SLOT connections to link layer and field combos
        self.cbo_points.layerChanged.connect(self.cbo_target_field.setLayer)        
        self.cbo_polygons.layerChanged.connect(self.cbo_source_field.setLayer)
        
        # When users clic on dialog's OK button...
        self.accepted.connect(self.process)
  
    def process(self):
        points = self.cbo_points.currentLayer()
        polygons = self.cbo_polygons.currentLayer()
        points_field = self.cbo_target_field.currentField()
        polygons_field = self.cbo_source_field.currentField()

        if not points or not points_field:
            self.iface.messageBar().pushWarning("Spatial Join", 
                "You should  select a point layer and a field where to store polygon's data!")
            return

        if not polygons or not polygons_field:
            self.iface.messageBar().pushWarning("Spatial Join", 
                "You should select a polygon layer and a field from where to get data!")
            return

        fs_polygons = [f for f in polygons.getFeatures()]
        point_field_idx = points.fields().indexOf(points_field)

        # Only for demo purposes, as in practice it would be better
        # to use processing algorithms, or spatial indexes
        with edit(points):
            for point in points.getFeatures(): 
                for polygon in fs_polygons:
                    if point.geometry().intersects(polygon.geometry()):
                        points.changeAttributeValue(point.id(), 
                                                    point_field_idx, 
                                                    polygon[polygons_field])
                        break

        self.iface.messageBar().pushSuccess("Spatial Join", "Polygon values have been transferred to points layer!")

