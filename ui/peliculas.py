# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peliculas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 600)
        MainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(MainWindow)
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
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 181, 27))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 10, 88, 27))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 280, 231, 27))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 320, 113, 27))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 360, 113, 27))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 360, 88, 27))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem7.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 400, 411, 101))
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty(u"showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 50, 141, 181))
        self.label.setTextFormat(Qt.MarkdownText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 24))
        self.menuPeliculas = QMenu(self.menubar)
        self.menuPeliculas.setObjectName(u"menuPeliculas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPeliculas.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.Peliculas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ficha", None));
        ___qtablewidgetitem1 = self.Peliculas.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.Peliculas.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Actor", None));
        ___qtablewidgetitem3 = self.Peliculas.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sinopsis", None));
        ___qtablewidgetitem4 = self.Peliculas.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Puntuaci\u00f3n", None));
        ___qtablewidgetitem5 = self.Peliculas.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Extras", None));

        __sortingEnabled = self.Peliculas.isSortingEnabled()
        self.Peliculas.setSortingEnabled(False)
        self.Peliculas.setSortingEnabled(__sortingEnabled)

        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Ingresar t\u00edtulo", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda de pelicula por actores", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Actor 1:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Actor 2:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pel\u00edculas Comunes", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Posters", None))
        self.menuPeliculas.setTitle(QCoreApplication.translate("MainWindow", u"Peliculas", None))
    # retranslateUi

