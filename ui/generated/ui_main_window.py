# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 678)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnOpenExcel = QPushButton(self.centralwidget)
        self.btnOpenExcel.setObjectName(u"btnOpenExcel")

        self.verticalLayout.addWidget(self.btnOpenExcel)

        self.lblFile = QLabel(self.centralwidget)
        self.lblFile.setObjectName(u"lblFile")

        self.verticalLayout.addWidget(self.lblFile)

        self.tableData = QTableWidget(self.centralwidget)
        self.tableData.setObjectName(u"tableData")

        self.verticalLayout.addWidget(self.tableData)

        self.btnPrint = QPushButton(self.centralwidget)
        self.btnPrint.setObjectName(u"btnPrint")

        self.verticalLayout.addWidget(self.btnPrint)

        self.btnPreview = QPushButton(self.centralwidget)
        self.btnPreview.setObjectName(u"btnPreview")

        self.verticalLayout.addWidget(self.btnPreview)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 997, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Paya Printer v0.3", None))
        self.btnOpenExcel.setText(QCoreApplication.translate("MainWindow", u"\u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0641\u0627\u06cc\u0644 \u0627\u06a9\u0633\u0644", None))
        self.lblFile.setText(QCoreApplication.translate("MainWindow", u"\u0647\u06cc\u0686 \u0641\u0627\u06cc\u0644\u06cc \u0627\u0646\u062a\u062e\u0627\u0628 \u0646\u0634\u062f\u0647 ", None))
        self.btnPrint.setText(QCoreApplication.translate("MainWindow", u"\u0686\u0627\u067e", None))
        self.btnPreview.setText(QCoreApplication.translate("MainWindow", u"\u067e\u06cc\u0634 \u0646\u0645\u0627\u06cc\u0634", None))
    # retranslateUi

