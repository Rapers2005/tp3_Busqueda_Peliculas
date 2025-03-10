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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_PeliculasWindow(object):
    def setupUi(self, PeliculasWindow):
        if not PeliculasWindow.objectName():
            PeliculasWindow.setObjectName(u"PeliculasWindow")
        PeliculasWindow.resize(641, 600)
        PeliculasWindow.setIconSize(QSize(24, 24))
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
        self.Peliculas.setGeometry(QRect(20, 50, 371, 181))
        self.Peliculas.setRowCount(5)
        self.Peliculas.setColumnCount(1)
        self.Peliculas.horizontalHeader().setStretchLastSection(True)
        self.Peliculas.verticalHeader().setVisible(True)
        self.Peliculas.verticalHeader().setCascadingSectionResizes(False)
        self.Peliculas.verticalHeader().setProperty(u"showSortIndicator", False)
        self.Peliculas.verticalHeader().setStretchLastSection(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 480, 88, 27))
        self.PeliculasComunes = QTableWidget(self.centralwidget)
        if (self.PeliculasComunes.columnCount() < 1):
            self.PeliculasComunes.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem7.setFont(font);
        self.PeliculasComunes.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        if (self.PeliculasComunes.rowCount() < 2):
            self.PeliculasComunes.setRowCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.PeliculasComunes.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.PeliculasComunes.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.PeliculasComunes.setItem(0, 0, __qtablewidgetitem10)
        self.PeliculasComunes.setObjectName(u"PeliculasComunes")
        self.PeliculasComunes.setGeometry(QRect(30, 320, 411, 101))
        self.PeliculasComunes.setTabKeyNavigation(True)
        self.PeliculasComunes.setProperty(u"showDropIndicator", True)
        self.PeliculasComunes.setDragDropOverwriteMode(True)
        self.PeliculasComunes.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.PeliculasComunes.horizontalHeader().setDefaultSectionSize(350)
        self.PeliculasComunes.horizontalHeader().setHighlightSections(True)
        self.labelPoster = QLabel(self.centralwidget)
        self.labelPoster.setObjectName(u"labelPoster")
        self.labelPoster.setGeometry(QRect(470, 50, 141, 181))
        self.labelPoster.setTextFormat(Qt.MarkdownText)
        self.labelTituloActores = QLabel(self.centralwidget)
        self.labelTituloActores.setObjectName(u"labelTituloActores")
        self.labelTituloActores.setGeometry(QRect(10, 260, 411, 19))
        self.labelTituloTitulo2 = QLabel(self.centralwidget)
        self.labelTituloTitulo2.setObjectName(u"labelTituloTitulo2")
        self.labelTituloTitulo2.setGeometry(QRect(40, 10, 411, 19))
        PeliculasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PeliculasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 24))
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
        ___qtablewidgetitem = self.Peliculas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PeliculasWindow", u"Ficha", None));
        ___qtablewidgetitem1 = self.Peliculas.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PeliculasWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.Peliculas.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PeliculasWindow", u"Actor", None));
        ___qtablewidgetitem3 = self.Peliculas.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PeliculasWindow", u"Sinopsis", None));
        ___qtablewidgetitem4 = self.Peliculas.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PeliculasWindow", u"Recaudaci\u00f3n", None));
        ___qtablewidgetitem5 = self.Peliculas.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PeliculasWindow", u"Extras", None));

        __sortingEnabled = self.Peliculas.isSortingEnabled()
        self.Peliculas.setSortingEnabled(False)
        self.Peliculas.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("PeliculasWindow", u"Cerrar", None))
        ___qtablewidgetitem6 = self.PeliculasComunes.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PeliculasWindow", u"Pel\u00edculas Comunes", None));
        ___qtablewidgetitem7 = self.PeliculasComunes.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PeliculasWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem8 = self.PeliculasComunes.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PeliculasWindow", u"A\u00f1o", None));

        __sortingEnabled1 = self.PeliculasComunes.isSortingEnabled()
        self.PeliculasComunes.setSortingEnabled(False)
        self.PeliculasComunes.setSortingEnabled(__sortingEnabled1)

        self.labelPoster.setText(QCoreApplication.translate("PeliculasWindow", u"Posters", None))
        self.labelTituloActores.setText(QCoreApplication.translate("PeliculasWindow", u"\"Resultado de la b\u00fasqueda Actores\"", None))
        self.labelTituloTitulo2.setText(QCoreApplication.translate("PeliculasWindow", u"\"Resultados de la b\u00fasqueda Titulo\"", None))
        self.menuPeliculas.setTitle(QCoreApplication.translate("PeliculasWindow", u"Resultado de Busqueda", None))
    # retranslateUi

