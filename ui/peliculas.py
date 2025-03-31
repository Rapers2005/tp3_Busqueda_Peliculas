# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_peliculas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_PeliculasWindow(object):
    def setupUi(self, PeliculasWindow):
        if not PeliculasWindow.objectName():
            PeliculasWindow.setObjectName(u"PeliculasWindow")
        PeliculasWindow.resize(429, 349)
        PeliculasWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(PeliculasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 181, 27))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 250, 88, 27))
        self.TituloActores = QLineEdit(self.centralwidget)
        self.TituloActores.setObjectName(u"TituloActores")
        self.TituloActores.setGeometry(QRect(10, 160, 113, 27))
        self.TituloActores_2 = QLineEdit(self.centralwidget)
        self.TituloActores_2.setObjectName(u"TituloActores_2")
        self.TituloActores_2.setGeometry(QRect(10, 200, 113, 27))
        self.labelTituloActores = QLabel(self.centralwidget)
        self.labelTituloActores.setObjectName(u"labelTituloActores")
        self.labelTituloActores.setGeometry(QRect(10, 120, 115, 19))
        self.labelTituloActores.setFrameShadow(QFrame.Plain)
        self.LimpiarBusqueda = QPushButton(self.centralwidget)
        self.LimpiarBusqueda.setObjectName(u"LimpiarBusqueda")
        self.LimpiarBusqueda.setGeometry(QRect(10, 250, 141, 27))
        self.labelTituloTitulo = QLabel(self.centralwidget)
        self.labelTituloTitulo.setObjectName(u"labelTituloTitulo")
        self.labelTituloTitulo.setGeometry(QRect(10, 30, 123, 19))
        PeliculasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PeliculasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 429, 24))
        self.menuPeliculas = QMenu(self.menubar)
        self.menuPeliculas.setObjectName(u"menuPeliculas")
        PeliculasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PeliculasWindow)
        self.statusbar.setObjectName(u"statusbar")
        PeliculasWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPeliculas.menuAction())

        self.retranslateUi(PeliculasWindow)

        QMetaObject.connectSlotsByName(PeliculasWindow)
    # setupUi

    def retranslateUi(self, PeliculasWindow):
        PeliculasWindow.setWindowTitle(QCoreApplication.translate("PeliculasWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("PeliculasWindow", u"Buscar", None))
        self.TituloActores.setText("")
        self.TituloActores.setPlaceholderText("")
        self.TituloActores_2.setText("")
        self.TituloActores_2.setPlaceholderText("")
        self.labelTituloActores.setText(QCoreApplication.translate("PeliculasWindow", u"\"Ingrese actores\"", None))
        self.LimpiarBusqueda.setText(QCoreApplication.translate("PeliculasWindow", u"Limpiar Busqueda ", None))
        self.labelTituloTitulo.setText(QCoreApplication.translate("PeliculasWindow", u"\"Ingrese un titulo\"", None))
        self.menuPeliculas.setTitle(QCoreApplication.translate("PeliculasWindow", u"Peliculas", None))
    # retranslateUi

