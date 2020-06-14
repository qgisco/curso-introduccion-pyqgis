from qgis.PyQt.QtWidgets import QMessageBox

reply = QMessageBox.question(None, 
            "Pregunta",
            "¿Quieres abrir la página de Wikipedia del aeropuerto '[%name%]'?",
            QMessageBox.Yes, QMessageBox.No)

if reply == QMessageBox.Yes:
    import webbrowser
    webbrowser.open("[%wikipedia%]")
