# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peliculas2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QToolBar, QVBoxLayout, QWidget)

class Ui_PeliculasWindow(object):
    def setupUi(self, PeliculasWindow):
        if not PeliculasWindow.objectName():
            PeliculasWindow.setObjectName(u"PeliculasWindow")
        PeliculasWindow.resize(632, 526)
        PeliculasWindow.setIconSize(QSize(24, 24))
        self.actionResultado = QAction(PeliculasWindow)
        self.actionResultado.setObjectName(u"actionResultado")
        self.centralwidget = QWidget(PeliculasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Peliculas = QTableWidget(self.centralwidget)
        if (self.Peliculas.columnCount() < 1):
            self.Peliculas.setColumnCount(1)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.Peliculas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.Peliculas.rowCount() < 5):
            self.Peliculas.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.Peliculas.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.Peliculas.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.Peliculas.setVerticalHeaderItem(2, __qtablewidgetitem3)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.Peliculas.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.Peliculas.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.Peliculas.setItem(0, 0, __qtablewidgetitem6)
        self.Peliculas.setObjectName(u"Peliculas")
        self.Peliculas.setGeometry(QRect(20, 60, 391, 271))
        self.Peliculas.setRowCount(5)
        self.Peliculas.setColumnCount(1)
        self.Peliculas.horizontalHeader().setStretchLastSection(True)
        self.Peliculas.verticalHeader().setVisible(True)
        self.Peliculas.verticalHeader().setCascadingSectionResizes(False)
        self.Peliculas.verticalHeader().setProperty(u"showSortIndicator", False)
        self.Peliculas.verticalHeader().setStretchLastSection(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 370, 88, 27))
        self.labelTituloTitulo2 = QLabel(self.centralwidget)
        self.labelTituloTitulo2.setObjectName(u"labelTituloTitulo2")
        self.labelTituloTitulo2.setGeometry(QRect(40, 10, 131, 19))
        self.frameposterContainer = QFrame(self.centralwidget)
        self.frameposterContainer.setObjectName(u"frameposterContainer")
        self.frameposterContainer.setGeometry(QRect(450, 60, 141, 111))
        self.frameposterContainer.setFrameShape(QFrame.StyledPanel)
        self.frameposterContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frameposterContainer)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 121, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        PeliculasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PeliculasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 632, 24))
        self.menuPeliculas = QMenu(self.menubar)
        self.menuPeliculas.setObjectName(u"menuPeliculas")
        PeliculasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PeliculasWindow)
        self.statusbar.setObjectName(u"statusbar")
        PeliculasWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(PeliculasWindow)
        self.toolBar.setObjectName(u"toolBar")
        PeliculasWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuPeliculas.menuAction())

        self.retranslateUi(PeliculasWindow)

        QMetaObject.connectSlotsByName(PeliculasWindow)
    # setupUi

    def retranslateUi(self, PeliculasWindow):
        PeliculasWindow.setWindowTitle(QCoreApplication.translate("PeliculasWindow", u"MainWindow", None))
        self.actionResultado.setText(QCoreApplication.translate("PeliculasWindow", u"Resultado", None))
        ___qtablewidgetitem = self.Peliculas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PeliculasWindow", u"Ficha", None));
        ___qtablewidgetitem1 = self.Peliculas.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PeliculasWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.Peliculas.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PeliculasWindow", u"Actor", None));
        ___qtablewidgetitem3 = self.Peliculas.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PeliculasWindow", u"Sinopsis", None));
        ___qtablewidgetitem4 = self.Peliculas.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PeliculasWindow", u"Puntuaci\u00f3n", None));
        ___qtablewidgetitem5 = self.Peliculas.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PeliculasWindow", u"Duraci\u00f3n", None));

        __sortingEnabled = self.Peliculas.isSortingEnabled()
        self.Peliculas.setSortingEnabled(False)
        self.Peliculas.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("PeliculasWindow", u"Cerrar", None))
        self.labelTituloTitulo2.setText(QCoreApplication.translate("PeliculasWindow", u"\"Por Titulo\"", None))
        self.menuPeliculas.setTitle(QCoreApplication.translate("PeliculasWindow", u"Resultado ", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("PeliculasWindow", u"toolBar", None))
    # retranslateUi

