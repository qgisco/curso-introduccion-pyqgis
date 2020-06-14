from qgis.core import QgsFeatureSink
from qgis.processing import alg

@alg(name='pruebaCopyLayer', label='Copy vector layer',
     group='examplescripts', group_label='Example scripts')
# 'INPUT' is the recommended name for the main input parameter
@alg.input(type=alg.VECTOR_LAYER, name='INPUT', label='Input vector layer')
@alg.input(type=alg.SINK, name='SINK', label='Copy of the vector layer')
# 'OUTPUT' is the recommended name for the main output parameter
@alg.output(type=alg.VECTOR_LAYER, name='OUTPUT', label='Output vector layer')
def pruebaCopyLayer(instance, parameters, context, feedback, inputs):
    """
    Copies a vector layer.
    """
    source = instance.parameterAsVectorLayer(
        parameters,
        'INPUT',
        context
    )
    (sink, dest_id) = instance.parameterAsSink(
                        parameters,
                        'SINK',
                        context,
                        source.fields(),
                        source.wkbType(),
                        source.sourceCrs())

    features = [f for f in source.getFeatures()]
    sink.addFeatures(features, QgsFeatureSink.FastInsert)
    return {'OUTPUT': dest_id}
