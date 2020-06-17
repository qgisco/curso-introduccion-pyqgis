# Cuidado con las 2 siguientes líneas. 
# En el taller las ejecutamos en consola, 
# cambiando manualmente la capa activa

aeropuertos = iface.activeLayer() #Falta incluir la URL de las capas para desarrollar el taller 
provincias = iface.activeLayer()

# La siguiente línea se ejecutó luego de haber 
# seleccionado el departamento de Santander 
# manualmente en el mapa
f_s = provincias.selectedFeatures()[0]

g_s = f_s.geometry()

fs_a = [f for f in aeropuertos.getFeatures()]

for f_a in fs_a: 
    res = f_a.geometry().intersects(g_s)
    if res:
        print(f_a["name"])
