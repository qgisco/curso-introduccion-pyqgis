"""
PREREQUISITE: Configure the environment so that Python can access QGIS libraries.

FOR WINDOWS:
    Open the OSGeo Shell and run the python-qgis-ltr.bat file, or just execute python-qgis-ltr.bat from the file explorer

FOR LINUX:
    You need to prepare the environment with PYTHONPATH and LD_LIBRARY_PATH variables. For example:
       export PYTHONPATH=/docs/dev/qgis/QGIS/3_14_0/output/python/
       export LD_LIBRARY_PATH=/docs/dev/qgis/QGIS/3_14_0/lib/
"""
from qgis.core import (QgsApplication, QgsVectorLayer)

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix
# Hint: print(QgsApplication.showSettings())
QgsApplication.setPrefixPath('/docs/dev/qgis/QGIS/3_14_0/output', True)
qgs = QgsApplication([], False)  # No GUI
qgs.initQgis()

airport_layer = QgsVectorLayer("/docs/tr/qgis_col/eventos/talleres/Semana_ICG_2019/data/sample_data_4326.gpkg|layername=Airports", "airport", "ogr")

print("\n\n\n############### RESULTADOS ####################")
print("\nLayer is valid:", airport_layer.isValid())
print("Layer CRS:", airport_layer.crs().description())
print("Layer's feature count:", airport_layer.featureCount())
print("\n       NOMBRE        \t\t\t              GEOMETRÍA")
for f in airport_layer.getFeatures():
    print(f['name'], '\t\t\t', f.geometry().asWkt())
print("\n\n\n#############################################")

qgs.exit()
