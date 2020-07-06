# Obtener capa activa. ¿Capa activa es None?
layer_a = iface.activeLayer()
if layer_a is None:
  print("No hay capa activa")
else:
  print("La capa activa es:", layer_a.name())


# featureCount()
print("El número de registros en la capa activa es:", layer_a.featureCount())


# Número de campos
print("El número de campos en la capa activa es:", len(layer_a.fields()))


# Nombre de todos los campos
for field in layer_a.fields():
  print(field.name())
  

# Acceder a atributos
feature = layer_a.getFeature(1)
print(feature["name"])


# Nombre de todos los aeropuertos
for feature in layer_a.getFeatures():
  print(feature["name"])


# Nombre y coords de todos los aeropuertos
for feature in layer_a.getFeatures():
  print(feature["name"], "-", feature.geometry().asWkt())
  

# Selección de departamento de Antioquia por expresión
layer_d = QgsProject.instance().mapLayersByName("Provinces")[0]
layer_d.selectByExpression("name = 'Antioquia'")


# Leer geometría seleccionada
dpto = layer_d.selectedFeatures()[0].geometry()


# ¿Qué aeropuertos se intersectan con el departamento seleccionado?
for aeropuerto in layer_a.getFeatures():
	if aeropuerto.geometry().intersects(dpto):
		print(aeropuerto['name'])


# Listar parejas:  Aeropuerto --> Departamento
for dpto in layer_d.getFeatures():
    for aeropuerto in layer_a.getFeatures():
        if aeropuerto.geometry().intersects(dpto.geometry()):
            print(aeropuerto['name'], "-->", dpto['name'])


# Campo nuevo --> "dpto"
layer_a.dataProvider().addAttributes([QgsField("dpto", QVariant.String)])
la.updateFields()


# ¿Cómo actualizar el valor de un campo?
dpto_idx = layer_a.fields().indexOf('dpto')

with edit(layer_a):
  layer_a.changeAttributeValue(1, dpto_idx, 'Santander')


# Llenar en el campo nuevo el nombre del departamento
with edit(layer_a):
  for dpto in layer_d.getFeatures():
    for aeropuerto in layer_a.getFeatures():
      if aeropuerto.geometry().intersects(dpto.geometry()):
        layer_a.changeAttributeValue(aeropuerto.id(), dpto_idx, departamento['name'])
        break  


# Otra manera (sin buffer de edición)
attr_values = {}
for dpto in layer_d.getFeatures():
  for aeropuerto in layer_a.getFeatures():
    if aeropuerto.geometry().intersects(dpto.geometry()):
      attr_values[aeropuerto.id()] = {dpto_idx: departamento['name']}
      break

layer_a.dataProvider().changeAttributeValues(attr_values)
                

