#!/usr/bin/env python3
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys, os, subprocess
import KatanaLauncherMain as klm
import KatanaLauncherSettings as Kls
from pathlib import Path

class KatanaLauncher(QtWidgets.QMainWindow):

    def __init__(self):
        super(KatanaLauncher, self).__init__()
        loadUi('KatanaLauncher.ui', self)

        #ensure script folders exist, and create if not
        if os.path.isdir('../scripts') == False:
            os.mkdir('../scripts')
        if os.path.isdir('../scripts/Renderers') == False:
            os.mkdir('../scripts/Renderers')

        self.refreshInputs()
        self.refresh_BTN.clicked.connect(self.refreshInputs)
        self.renderer_CB.currentTextChanged.connect(self.renderer_changed)
        self.run_BTN.pressed.connect(self.launch)
        self.settings_BTN.pressed.connect(self.settingsWindow)

    def location_on_the_screen(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def renderer_changed(self,index):
        # After the combobox changes, find the versions for chosen renderer
        self.renderer_version_CB.clear()
        if index == '3Delight':
            self.renderer_version_CB.addItem('Katana Version')
            self.renderer_version_CB.setEnabled(False)
        elif index == 'Renderman':
            self.renderer_version_CB.addItems(klm.getPrmanVersions())
            self.renderer_version_CB.setEnabled(True)
        elif index == 'Redshift':
            self.renderer_version_CB.addItems(klm.getRedshiftVersions())
            self.renderer_version_CB.setEnabled(True)
        elif index == 'Arnold':
            self.renderer_version_CB.addItems(klm.getArnoldVersions())
            self.renderer_version_CB.setEnabled(True)
        else:
            self.renderer_version_CB.setEnabled(False)
        

    def refreshInputs(self):
        #clear scripts
        while self.scripts_layout.count():
            child = self.scripts_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        #clear versions
        self.katana_version_CB.clear()
        self.renderer_CB.clear()
        
        #get scripts
        for script in klm.getBatchScripts():
            CheckBox = QtWidgets.QCheckBox(script)
            self.scripts_layout.addWidget(CheckBox)
        self.scripts_layout.addStretch()

        #get versions
        self.katana_version_CB.addItems(klm.getKatanaVersions())
        self.renderer_CB.addItems(klm.getRenderers())

    def settingsWindow(self):
        settings.show()

    def launch(self):
            katana_version = self.katana_version_CB.currentText()
            renderer = self.renderer_CB.currentText()
            render_version = self.renderer_version_CB.currentText()
            os.environ['KATANA_VERSION'] = katana_version
            os.environ['RENVER'] = render_version
            command = ''
            # read all needed script files, combine them into one string and execute
            for i in range (self.scripts_layout.count() - 1):
                script = self.scripts_layout.itemAt(i).widget()
                if script.isChecked():
                    command += Path(klm.paths['scripts_path'] + '/' +script.text()).read_text()
            command += Path(klm.paths['scripts_path'] + '/Renderers/' + renderer + '.sh').read_text()
            print(command)
            #Run command as subprocess so you can launch more than one.
            #os.system('gnome-terminal -- ' + command)
            subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = KatanaLauncher()
    settings = Kls.KatanaLauncherSettings()
    # repositions windows to center of the screen
    ui.location_on_the_screen()
    settings.location_on_the_screen()

    ui.show()
    app.exec_()


