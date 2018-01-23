__author__ = 'alefur'

from PyQt5.QtWidgets import QGridLayout, QWidget, QGroupBox, QLineEdit, QPushButton

from widgets import ValueGB

class Device(QGroupBox):
    def __init__(self, title):
        QGroupBox.__init__(self)
        self.setTitle(title)
        self.grid = QGridLayout()

class Example(QWidget):
    def __init__(self, mainTree):
        QWidget.__init__(self)
        self.mainTree = mainTree
        self.mainLayout = QGridLayout()

        self.mainLayout.addWidget(ValueGB('Enabled ', self.actor.models['xcu_r0'], 'ionpump1', 0, '{:g}'), 0, 0)
        self.mainLayout.addWidget(ValueGB('Voltage(V)', self.actor.models['xcu_r0'], 'ionpump1', 1, '{:g}'), 0, 1)
        self.mainLayout.addWidget(ValueGB('Current(A)', self.actor.models['xcu_r0'], 'ionpump1', 2, '{:g}'), 0, 2)
        self.mainLayout.addWidget(ValueGB('Temperature(K)', self.actor.models['xcu_r0'], 'ionpump1', 3, '{:g}'), 0, 3)
        self.mainLayout.addWidget(ValueGB('Pressure(Torr)', self.actor.models['xcu_r0'], 'ionpump1', 4, '{:g}'), 0, 4)

        self.mainLayout.addWidget(ValueGB('Enabled ', self.actor.models['xcu_r0'], 'ionpump2', 0, '{:g}'), 1, 0)
        self.mainLayout.addWidget(ValueGB('Voltage(V)', self.actor.models['xcu_r0'], 'ionpump2', 1, '{:g}'), 1, 1)
        self.mainLayout.addWidget(ValueGB('Current(A)', self.actor.models['xcu_r0'], 'ionpump2', 2, '{:g}'), 1, 2)
        self.mainLayout.addWidget(ValueGB('Temperature(K)', self.actor.models['xcu_r0'], 'ionpump2', 3, '{:g}'), 1, 3)
        self.mainLayout.addWidget(ValueGB('Pressure(Torr)', self.actor.models['xcu_r0'], 'ionpump2', 4, '{:g}'), 1, 4)

        self.mainLayout.addWidget(ValueGB('Cooler_Setpoint(K)', self.actor.models['xcu_r0'], 'coolerTemps', 0, '{:g}'), 2, 0)
        self.mainLayout.addWidget(ValueGB('Cooler_Reject(C)', self.actor.models['xcu_r0'], 'coolerTemps', 1, '{:g}'), 2, 1)
        self.mainLayout.addWidget(ValueGB('Cooler_Tip(K)', self.actor.models['xcu_r0'], 'coolerTemps', 2, '{:g}'), 2, 2)
        self.mainLayout.addWidget(ValueGB('Cooler_Power(W)', self.actor.models['xcu_r0'], 'coolerTemps', 3, '{:g}'), 2, 3)

        self.commandLine = QLineEdit()
        self.commandButton = QPushButton('Send Command')
        self.commandButton.clicked.connect(self.sendCommand)

        self.mainLayout.addWidget(self.commandLine, 3,0,1,3)
        self.mainLayout.addWidget(self.commandButton, 3,3,1,1)
        self.setLayout(self.mainLayout)

    @property
    def actor(self):
        return self.mainTree.actor

    def sendCommand(self):
        [actor, cmdStr] = self.commandLine.text().split(' ', 1)
        self.actor.threadCmd(**dict(actor=actor, cmdStr=cmdStr))