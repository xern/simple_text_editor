#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A Text Editor, written in Python 3 using the Qt5 framework.
This is the main file of this project.
Version: 1.0.1
Python 3.6+
Date created: 21.08.2019
"""

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPlainTextEdit, QMessageBox,
                             QAction, QFileDialog, qApp)


def about_dialog():
    text = "<center>" \
           "<h1>Simple Text Editor</h1>" \
           "&#8291;" \
           "</center>" \
           "<p>Version 1.0.1<br/>" \
           "Created by niftycode<br/>" \
           "MIT License</p>"
    QMessageBox.about(window, "About Simple Text Editor", text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the TextEdit widget
        self.text_widget = QPlainTextEdit()
        self.setCentralWidget(self.text_widget)

        self.title = 'Simple Text Editor'
        self.window_icon = 'img/editor-app-icon.png'
        self.left = 300
        self.top = 100
        self.width = 700
        self.height = 800

        self.file_path = None

        # Add actions
        self.quit_action = QAction('&Quit', self)
        self.about_action = QAction('&About', self)
        self.open_action = QAction('&Open', self)
        self.save_action = QAction('&Save', self)
        self.save_as_action = QAction('Save as', self)

        self.create_actions()
        self.init_ui()

    def create_actions(self):
        # Quit action
        self.quit_action.setShortcut('Ctrl+Q')
        self.quit_action.setStatusTip('Exit this application.')
        self.quit_action.triggered.connect(qApp.quit)

        # About action
        self.about_action.setShortcut('Ctrl+A')
        self.about_action.setStatusTip('About this application.')
        self.about_action.triggered.connect(about_dialog)

        # Open file action
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setStatusTip('Open a file.')
        self.open_action.triggered.connect(self.open_file)

        # Save file action
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save a file.')
        self.save_action.triggered.connect(self.save_file)

        # Save file as action
        self.save_as_action.setStatusTip('Save file as')
        self.save_as_action.triggered.connect(self.save_file_as)

    def create_menubar(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        self.help_menu.addAction(self.about_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addAction(self.quit_action)

    def init_ui(self):
        # Create menus
        self.file_menu = self.menuBar().addMenu("&File")
        self.help_menu = self.menuBar().addMenu("&Help")
        self.create_menubar()

        # Set basic window layout
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.window_icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()

    def open_file(self):
        path = QFileDialog.getOpenFileName(window, "Open")[0]
        if path:
            self.text_widget.setPlainText(open(path).read())
            self.file_path = path

    def save_file(self):
        if self.file_path is None:
            self.save_file_as()
        else:
            with open(self.file_path, "w") as f:
                f.write(self.text_widget.toPlainText())
            self.text_widget.document().setModified(False)

    def save_file_as(self):
        path = QFileDialog.getSaveFileName(window, "Save As")[0]
        if path:
            self.file_path = path
            self.save_file()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
