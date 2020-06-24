from .plugin import SpatialJoin

def classFactory(iface):
    return SpatialJoin(iface)

