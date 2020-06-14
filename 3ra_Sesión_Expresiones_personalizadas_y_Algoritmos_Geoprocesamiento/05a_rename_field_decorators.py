from qgis.core import edit
from qgis.processing import alg

@alg(name='pruebaRenameField', label='Rename field from vector layer',
     group='examplescripts', group_label='Example scripts')
# 'INPUT' is the recommended name for the main input parameter
@alg.input(type=alg.VECTOR_LAYER, name='INPUT', label='Input vector layer')
@alg.input(type=alg.FIELD, name='INPUT_FIELD', label='Input field', 
           parentLayerParameterName='INPUT')
@alg.input(type=alg.STRING, name='NEW_FIELD_NAME', label='New field name',
           default='new_field')
# 'OUTPUT' is the recommended name for the main output parameter
@alg.output(type=alg.VECTOR_LAYER, name='OUTPUT',
            label='Vector layer with field renamed')
def pruebaRenameField(instance, parameters, context, feedback, inputs):
    """
    Renames fields.
    """
    source = instance.parameterAsVectorLayer(
        parameters,
        'INPUT',
        context
    )
    input_field = instance.parameterAsFields(
            parameters,
            'INPUT_FIELD',
            context)[0]
    new_name = instance.parameterAsString(
            parameters,
            'NEW_FIELD_NAME',
            context)
    
    if input_field == new_name:
        feedback.reportError("El nuevo nombre para el campo coincide con el existente...")
        return {'OUTPUT': None}

    # Rename the field
    with edit(source):
        source.renameAttribute(source.fields().indexFromName(input_field), new_name)

    return {'OUTPUT': source}
