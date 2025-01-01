from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog
import os
import mods.execExt as execExt

def main():
    print("hello")
    
def addGame(gameName, playClickTrigger):
    gameWidget = QWidget()
    gameLayout = QVBoxLayout(gameWidget)
    gameNameLabel = QLabel(gameName)
    gameLayout.addWidget(gameNameLabel)
    playButton = QPushButton("Play")
    playButton.clicked.connect(playClickTrigger)
    gameLayout.addWidget(playButton)
    return gameWidget

def renderGui():
    def openInstallDirectory():
        # Open directory dialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        directory = QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)
        directory = directory[0]
        if directory:
            # Execute the extension
            return directory
    def openExtension():
        directory = openInstallDirectory()
        # Open file dialog for .py files
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getOpenFileName(None, "Select Extension", "", "Python Files (*.py)", options=options)
        file = file[0]
        if directory:
            execExt.exec(file, directory)
    # Initialize the application
    app = QApplication([])
    window = QMainWindow()

    # Set the window title
    window.setWindowTitle("My App")

    # Create a central widget
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    # Create a layout for the central widget
    layout = QVBoxLayout(central_widget)

    # Create a widget for games list
    games_widget = QWidget()
    layout.addWidget(games_widget)
    
    # Create a button to install extension
    install_extension_button = QPushButton("Install Extension")
    install_extension_button.clicked.connect(openExtension)
    layout.addWidget(install_extension_button)
    
    def addWidget(widget):
        layout.addWidget(widget)
    def execute():
        # Show the window
        window.show()
        app.exec()
    
    return {
        "addWidget": addWidget,
        "execute": execute
    }