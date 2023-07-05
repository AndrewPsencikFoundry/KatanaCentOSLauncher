import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys, os, json

DEFAULT_PATHS = {'scripts_path' : '../scripts',
         'katana_path' : '/home/foundry/foundry',
         'arnold_path' : '/home/foundry/ktoa',
         'prman_path' : '/opt/pixar',
         'redshift_path' : '/usr/redshift/redshift4katana'
        }

class KatanaLauncherSettings(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(KatanaLauncherSettings, self).__init__()
        loadUi('KatanaLauncherSettings.ui', self)
        with open('../config.json', "w") as outfile:
            json.dump(DEFAULT_PATHS, outfile)
            self.paths = DEFAULT_PATHS

        #set text according to jsonfiles
        self.Katana_Bin_LE.setText(self.paths['katana_path'])
        self.Scripts_LE.setText(self.paths['scripts_path'])
        self.prman_LE.setText(self.paths['prman_path'])
        self.Arnold_LE.setText(self.paths['arnold_path'])
        #connect browse buttons
        self.Katana_Bin_BTN.clicked.connect(self.browseKatana)
        self.Scripts_BTN.clicked.connect(self.browseScripts)
        self.Arnold_BTN.clicked.connect(self.browseArnold)
        self.prman_BTN.clicked.connect(self.browsePrman)
        self.reset_default_BTN.clicked.connect(self.resetDefault)
        self.Save_BTN.clicked.connect(self.save)

    def location_on_the_screen(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def browseKatana(self):
        file = QtWidgets.QFileDialog
        file_path = file.getExistingDirectory(self,'Please Select Where Katana is Located')
        self.Katana_Bin_LE.setText(file_path)
        self.paths['katana_path'] = file_path

    def browseScripts(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self,'Scripts Folder')
        self.Scripts_LE.setText(fname)
        self.paths['scripts_path'] = fname

    def browseArnold(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self,'Arnold Folder')
        self.Arnold_LE.setText(fname)
        self.paths['arnold_path'] = fname

    def browsePrman(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self,'Renderman Folder')
        self.prman_LE.setText(fname)
        self.paths['prman_path'] = fname

    def save(self):
        print('writing to config.json...')
        with open('../config.json', "w") as outfile:
            json.dump(self.paths, outfile)
        self.close()

    def resetDefault(self):
        print('Resetting to Default Paths...')
        with open('../config.json', "w") as outfile:
            json.dump(DEFAULT_PATHS, outfile)
        self.close()
