# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import math
from geographiclib.geodesic import Geodesic

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# lista de Satelites
satellites = dict()
satellites = {'-': 0,'Amazonas3': -61.0, 'Hispasat 30w-4': -30, 'Hispasat74W-1': -74, 'Amazonas5': -61, 'Hispasat55W-2': -55.5}
#Lista de ciudades
ciudad = dict()
ciudad = {'-': [0,0],'Loja': [-79.20,-3.99], 'Zamora': [-78.96,-4.07], 'Cuenca': [-79,-2.9], 'Machala': [-79.96,-3.26], 'Guayaquil': [-79.89,-2.18], 'Quito': [-78.48,-0.16]}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
    	#MainWindow=ventana principal se la redimenciona a 400x300 para q entren todos los objetos
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        # Caja desplegable vertical de lista de Satelites 
        self.sname = QtGui.QComboBox(self.groupBox)
        self.sname.setObjectName(_fromUtf8("sname"))
        self.sname.setEditable(False)
        for k,v in sorted(satellites.items()):
            self.sname.addItem(_fromUtf8(k))
        self.verticalLayout_3.addWidget(self.sname)
        #phaiss = variable de longitud de satelite
        self.phaiss = QtGui.QDoubleSpinBox(self.groupBox)
        self.phaiss.setMinimum(-180.0)
        self.phaiss.setMaximum(180.0)
        self.phaiss.setObjectName(_fromUtf8("phaiss"))
        self.verticalLayout_3.addWidget(self.phaiss)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))

        # Caja desplegable vertical de lista de ciudades 
        self.pname = QtGui.QComboBox(self.groupBox_2)
        self.pname.setObjectName(_fromUtf8("pname"))
        self.pname.setEditable(False)
        for k,v in sorted(ciudad.items()):
            self.pname.addItem(_fromUtf8(k))
        self.verticalLayout_11.addWidget(self.pname)        
        #ETIQUETA DE DATOS AUTOMATICOS POR CIUDAD
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_12.addWidget(self.label_11)
        #ETIQUETA DE LONGITUD
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_12.addWidget(self.label_13)
        #ETIQUETA DE LATITUD
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_12.addWidget(self.label_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.phaibs = QtGui.QDoubleSpinBox(self.groupBox_2)
        #phaibs = variable de longitud de ciudad
        self.phaibs.setMinimum(-180.0)
        self.phaibs.setMaximum(180.0)
        self.phaibs.setObjectName(_fromUtf8("phaibs"))
        self.verticalLayout_11.addWidget(self.phaibs)
        self.lbs = QtGui.QDoubleSpinBox(self.groupBox_2)
        #lbs = variable de latitud de ciudad
        self.lbs.setMinimum(-90.0)
        self.lbs.setMaximum(90.0)
        self.lbs.setObjectName(_fromUtf8("lbs"))
        self.verticalLayout_11.addWidget(self.lbs)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.calc = QtGui.QPushButton(self.splitter)
        self.calc.setObjectName(_fromUtf8("calc"))
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.splitter_3 = QtGui.QSplitter(self.groupBox_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.widget1 = QtGui.QWidget(self.splitter_3)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_21 = QtGui.QLabel(self.widget1)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_5.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.widget1)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_5.addWidget(self.label_22)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_23 = QtGui.QLabel(self.widget1)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_5.addWidget(self.label_23)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        #Etiquetas de azimut, elevacion y ditancia
        self.Azlabel = QtGui.QLabel(self.widget1)
        self.Azlabel.setFrameShape(QtGui.QFrame.Box)
        self.Azlabel.setFrameShadow(QtGui.QFrame.Plain)
        self.Azlabel.setObjectName(_fromUtf8("Azlabel"))
        self.horizontalLayout_9.addWidget(self.Azlabel)
        self.Ellabel = QtGui.QLabel(self.widget1)
        self.Ellabel.setFrameShape(QtGui.QFrame.Box)
        self.Ellabel.setObjectName(_fromUtf8("Ellabel"))
        self.horizontalLayout_9.addWidget(self.Ellabel)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.Dlabel = QtGui.QLabel(self.widget1)
        self.Dlabel.setFrameShape(QtGui.QFrame.Box)
        self.Dlabel.setObjectName(_fromUtf8("Dlabel"))
        self.horizontalLayout_9.addWidget(self.Dlabel)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.gridLayout_2.addWidget(self.splitter_3, 1, 0, 2, 2)
        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1562, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #si se clickea "calcular" el programa se dirige a realizar el proceso matematico
        self.calc.clicked.connect(self.calculations)
        #se obtiene los datos de ciudad y satelite escogido y se lo ubica en los recuadros correspondientes
        self.sname.currentIndexChanged.connect(self.combo)
        self.pname.currentIndexChanged.connect(self.combo2)        
    def combo(self):
        name = str(self.sname.currentText())
        value = float(satellites.get(name))
        self.phaiss.setValue(value)
    def combo2(self):
        name2 = str(self.pname.currentText())
        value2 = ciudad.get(name2)
        self.phaibs.setValue(value2[0]) #longitud 
        self.lbs.setValue(value2[1]) #latitud

        
    def calculations(self):
        Re=6378
        aGEO=42178  # radio terrestre + distancia tierra-satelite (r+h)
        Qss = self.phaiss.value() # longitud de satelite
        Qe = self.phaibs.value() # longitud de ciudad
        lamda = self.lbs.value() # latitud de ciudad
        p=Re/aGEO  #relacion distancias
        B= float(Qe)-float(Qss) # diferencia de longitudes (fi)
        A=math.degrees(math.atan(math.tan(math.radians(B))/math.sin(math.radians(lamda))))
        #Se usa la libreria geodesic para ubicar al punto de acuerdo a un cuadrante
        geod = Geodesic.WGS84
        g = geod.Inverse(0,Qss,lamda,Qe)
        if lamda>0 and g['azi1']>0:
            Az= 180+A #NorEste
            print("Cuadrante NorEste")
        elif lamda>0 and g['azi1']<0:
            Az=180-A # NorOeste
            print("Cuadrante NorOeste")
        elif lamda<0 and g['azi1']<0:
            Az=A 	#SurOeste
            print("Cuadrante SurOeste")
        elif lamda<0 and g['azi1']>0:
            Az=360-A #SurEste
            print("Cuadrante SurEste")
        print ("El angulo de azimut es : ", Az)
        self.Azlabel.setText(_fromUtf8(str(Az)))
        #la variable b se usa para calcular el angulo de elevacion y la distancia
        b=math.degrees(math.acos(math.cos(math.radians(B))*math.cos(math.radians(lamda))))
        print("b es: ",b)
        d=35800*math.sqrt(1+0.41999*(1-math.cos(math.radians(b))))
        print ("La distancia al satelite: ",d)
        self.Dlabel.setText(_fromUtf8(str(d)))
        EL=math.degrees(math.atan((math.cos(math.radians(b))-p)/math.sin(math.radians(b))))
        print ("El angulo de elevacion es: ",EL)
        self.Ellabel.setText(_fromUtf8(str(EL)))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Alineamiento de antena a satelite 1.0", None))
        self.groupBox.setTitle(_translate("MainWindow", "Informacion del Satelite", None))
        self.label.setText(_translate("MainWindow", "Satelite", None))
        self.label_2.setText(_translate("MainWindow", "Longitud", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Informacion del Usuario", None))
        self.label_11.setText(_translate("MainWindow", "Ciudad", None))
        self.label_13.setText(_translate("MainWindow", "Longitud Usuario", None))
        self.label_14.setText(_translate("MainWindow", "Latitud Usuario", None))
        self.calc.setText(_translate("MainWindow", "Calcular", None))

        self.groupBox_4.setTitle(_translate("MainWindow", "Resultados", None))
        self.label_21.setText(_translate("MainWindow", "Azimut", None))
        self.label_22.setText(_translate("MainWindow", "Elevacion", None))
        self.label_23.setText(_translate("MainWindow", "Distancia", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

