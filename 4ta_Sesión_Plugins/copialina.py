"""
QGIS MENUS
"""
# Insert menu to QGIS GUI
menu = QMenu('&Mis herramientas', iface.mainWindow())

# To last position
iface.mainWindow().menuBar().addMenu(menu)

# How to remove it
# last = iface.mainWindow().menuBar().actions()[-1]
# iface.mainWindow().menuBar().removeAction(last)

# Access and open QGIS action
about = iface.actionAbout()
about.trigger()

# Add action to our menu
menu.addAction(about)



"""
QGIS ToolBars
"""
# Add action to plugin toolbar
iface.addToolBarIcon(about)

# Remove action from plugin toolbar
iface.removeToolBarIcon(about)

# Custom Toolbar
toolbar = iface.addToolBar("Mi ToolBar")
toolbar.addAction(about)

# Remove Custom Toolbar
iface.mainWindow().removeToolBar(toolbar)



"""
Message Bar
"""
iface.messageBar().pushMessage("Mensaje")

iface.messageBar().pushMessage("Mensaje", duration=0)

iface.messageBar().pushInfo("Título", "Mensaje")

iface.messageBar().pushSuccess("Título", "Mensaje")

iface.messageBar().pushWarning("Título", "Mensaje")



"""
QGIS Project
"""
# Create and add layer to project
layer = QgsVectorLayer("/path/to/geopackage/file.gpkg|layername=Airports", "airport", "ogr")
QgsProject.instance().addMapLayer(layer)

# Project active layer
iface.activeLayer()

# Find layers by name
QgsProject.instance().mapLayersByName("airport")

# Get project layers
QgsProject.instance().mapLayers()

# Remove active layer
QgsProject.instance().removeMapLayer(iface.activeLayer().id())



"""
QGIS Layer tree (a.k.a., Layers panel/Legend/ToC)
"""
root = QgsProject.instance().layerTreeRoot()

# Add group
mi_grupo = root.addGroup("Mi grupo")

# Add layer to group
layer = QgsVectorLayer("/path/to/geopackage/file.gpkg|layername=Airports", "airport", "ogr")
mi_grupo.addLayer(layer)

# Add layer to root
layer1 = QgsVectorLayer("/path/to/geopackage/file.gpkg|layername=Airports", "airport", "ogr")
root.addLayer(layer1)

# Clear layer tree
root.clear()

