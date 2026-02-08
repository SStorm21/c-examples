from PyQt5 import QtCore , QtGui , QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
root = QtWidgets.QWidget()
root.show()
#width and hghit op
root.resize(700,600)#width and hghit
root.move(800,200) #left and Top

app.exec_()