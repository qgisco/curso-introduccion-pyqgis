# Fuente: https://gis.stackexchange.com/a/340615/4972

layer = QgsProject.instance().mapLayer('[% @layer_id %]')
layer.selectByExpression('"type"=\'[%type%]\'')
