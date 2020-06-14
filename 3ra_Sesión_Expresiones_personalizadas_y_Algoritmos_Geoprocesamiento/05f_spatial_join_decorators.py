from qgis.core import edit
from qgis.processing import alg

@alg(name='scriptSpatialJoin', label='Get attribute from overlay polygon',
     group='examplescripts', group_label='Example scripts')
# 'INPUT' is the recommended name for the main input parameter
@alg.input(type=alg.VECTOR_LAYER, name='INPUT', label='Input point layer', 
     types=[0])
@alg.input(type=alg.FIELD, name='TARGET_FIELD', label='Points target field', 
           parentLayerParameterName='INPUT')
@alg.input(type=alg.VECTOR_LAYER, name='INPUT_POLYGONS', label='Input polygon layer', 
     types=[2])
@alg.input(type=alg.FIELD, name='SOURCE_FIELD', label='Polygons source field', 
           parentLayerParameterName='INPUT_POLYGONS')
# 'OUTPUT' is the recommended name for the main output parameter
@alg.output(type=alg.VECTOR_LAYER, name='OUTPUT',
            label='Point layer with info from polygons')
def scriptSpatialJoin(instance, parameters, context, feedback, inputs):
    """
    Gets attributes from polygons and stores them into intersecting points.
    
    Of course we can use other processing tools to do the same, or we could 
    build spatial indexes for that, but this is just a sample script.
    """
    points = instance.parameterAsVectorLayer(
        parameters,
        'INPUT',
        context
    )
    points_field = instance.parameterAsFields(
            parameters,
            'TARGET_FIELD',
            context)[0]
    polygons = instance.parameterAsVectorLayer(
        parameters,
        'INPUT_POLYGONS',
        context
    )
    polygons_field = instance.parameterAsFields(
            parameters,
            'SOURCE_FIELD',
            context)[0]

    fs_polygons = [f for f in polygons.getFeatures()]
    point_field_idx = points.fields().indexOf(points_field)

    with edit(points):
        for point in points.getFeatures(): 
            for polygon in fs_polygons:
                if point.geometry().intersects(polygon.geometry()):
                    points.changeAttributeValue(point.id(), point_field_idx, polygon[polygons_field])
                    break

    return {'OUTPUT': points}
