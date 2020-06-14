from qgis.core import (qgsfunction, QgsProject, QgsRaster)

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def get_elevation(feature, parent):
    layers = QgsProject.instance().mapLayersByName("DEM")
    if layers: # Any layer called DEM?
        rLayer = layers[0]
        geom = feature.geometry()
        geom.convertToSingleType()  # Single points are required
        ident = rLayer.dataProvider().identify(geom.asPoint(), 
                                               QgsRaster.IdentifyFormatValue)
        if ident.isValid():
            return ident.results()[1]  # Read from band 1
    return NULL
