# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (edit,
                       QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterField,
                       QgsProcessingParameterString,
                       QgsProcessingOutputVectorLayer)
import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    INPUT_FIELD = 'INPUT_FIELD'
    NEW_FIELD_NAME = 'NEW_FIELD_NAME'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

    def name(self):
        return 'rename_field_class'

    def displayName(self):
        return self.tr('Rename Field (using classes)')

    def group(self):
        return self.tr('Example scripts')

    def groupId(self):
        return 'examplescripts'

    def shortHelpString(self):
        return self.tr("Rename Field (using classes)")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVector]
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                self.INPUT_FIELD,
                self.tr('Input field name'),
                parentLayerParameterName='INPUT',
                type=QgsProcessingParameterField.Numeric
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.NEW_FIELD_NAME,
                self.tr('New field name'),
                defaultValue='new_field'
            )
        )
        self.addOutput(
            QgsProcessingOutputVectorLayer(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsVectorLayer(
            parameters,
            self.INPUT,
            context
        )
        input_field = self.parameterAsFields(
                parameters,
                self.INPUT_FIELD,
                context)[0]
        new_name = self.parameterAsString(
                parameters,
                self.NEW_FIELD_NAME,
                context)

        if input_field == new_name:
            feedback.reportError("El nuevo nombre para el campo coincide con el existente...")
            return {'OUTPUT': None}
        
        # Rename the field
        with edit(source):
            source.renameAttribute(source.fields().indexFromName(input_field), new_name)

        return {self.OUTPUT: source}
