# Source: https://gis.stackexchange.com/a/279937/4972
import sys

from qgis.core import QgsApplication, QgsProject, QgsCoordinateReferenceSystem
from qgis.analysis import QgsNativeAlgorithms

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
qgis_prefix = '/docs/dev/qgis/QGIS/3_14_0/output'
QgsApplication.setPrefixPath(qgis_prefix, True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append(qgis_prefix + '/python/plugins')

import processing
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

# Set project CRS and measurement settings
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(4326))
QgsProject.instance().setEllipsoid("WGS84")

# You can see what parameters are needed by the algorithm  
# using: processing.algorithmHelp("native:sumlinelengths")
params = {'POLYGONS':'/docs/tr/qgis_col/eventos/talleres/3ra_jornada_talleres_internos/sample_data_4326.gpkg|layername=Provinces',
          'LINES':'/docs/tr/qgis_col/eventos/talleres/3ra_jornada_talleres_internos/sample_data_4326.gpkg|layername=Roads',
          'LEN_FIELD':'LENGTH',
          'COUNT_FIELD':'COUNT',
          'OUTPUT':'TEMPORARY_OUTPUT'}
res = processing.run("native:sumlinelengths", params)

for feature in res['OUTPUT'].getFeatures():
    print(feature['name'], feature['LENGTH'])

qgs.exit()
