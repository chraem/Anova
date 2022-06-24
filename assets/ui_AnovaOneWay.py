# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnovaOneWayACmykA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(186, 186, 186);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(186, 186, 186);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 10, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.reset_Btn = QPushButton(self.frame_2)
        self.reset_Btn.setObjectName(u"reset_Btn")
        self.reset_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_Btn.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"padding: 3px;\n"
"border-radius: 5px;")
        self.reset_Btn.setAutoDefault(False)
        self.reset_Btn.setFlat(True)

        self.gridLayout_2.addWidget(self.reset_Btn, 0, 8, 1, 1)

        self.generate_Btn = QPushButton(self.frame_2)
        self.generate_Btn.setObjectName(u"generate_Btn")
        self.generate_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate_Btn.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"padding: 3px;\n"
"border-radius: 5px;")
        self.generate_Btn.setFlat(True)

        self.gridLayout_2.addWidget(self.generate_Btn, 0, 6, 1, 1)

        self.compute_Btn = QPushButton(self.frame_2)
        self.compute_Btn.setObjectName(u"compute_Btn")
        self.compute_Btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.compute_Btn.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"padding: 3px;\n"
"border-radius: 5px;")
        self.compute_Btn.setFlat(True)

        self.gridLayout_2.addWidget(self.compute_Btn, 0, 7, 1, 1)

        self.row_Sbox = QSpinBox(self.frame_2)
        self.row_Sbox.setObjectName(u"row_Sbox")
        self.row_Sbox.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.row_Sbox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.row_Sbox.setAccelerated(False)
        self.row_Sbox.setProperty("showGroupSeparator", False)
        self.row_Sbox.setMaximum(10000)

        self.gridLayout_2.addWidget(self.row_Sbox, 0, 1, 1, 1)

        self.column_Sbox = QSpinBox(self.frame_2)
        self.column_Sbox.setObjectName(u"column_Sbox")
        self.column_Sbox.setCursor(QCursor(Qt.ArrowCursor))
        self.column_Sbox.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.column_Sbox.setWrapping(False)
        self.column_Sbox.setFrame(True)
        self.column_Sbox.setMaximum(10000)

        self.gridLayout_2.addWidget(self.column_Sbox, 0, 3, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 10, 5)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.header_Ledit = QLineEdit(self.frame_5)
        self.header_Ledit.setObjectName(u"header_Ledit")
        self.header_Ledit.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.header_Ledit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.header_Ledit)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_4 = QGridLayout(self.tab_1)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.rawData_Tbl = QTableWidget(self.tab_1)
        self.rawData_Tbl.setObjectName(u"rawData_Tbl")
        self.rawData_Tbl.setFrameShadow(QFrame.Plain)
        self.rawData_Tbl.horizontalHeader().setVisible(True)

        self.gridLayout_4.addWidget(self.rawData_Tbl, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.summary_Tbl = QTableWidget(self.tab_2)
        if (self.summary_Tbl.columnCount() < 5):
            self.summary_Tbl.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.summary_Tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.summary_Tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.summary_Tbl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.summary_Tbl.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.summary_Tbl.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.summary_Tbl.setObjectName(u"summary_Tbl")
        self.summary_Tbl.setFrameShape(QFrame.StyledPanel)
        self.summary_Tbl.setFrameShadow(QFrame.Plain)
        self.summary_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.summary_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.summary_Tbl, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 22, 0, 1, 1)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 17, 1, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 18, 1, 1, 1)

        self.N_Lbl = QLabel(self.frame_4)
        self.N_Lbl.setObjectName(u"N_Lbl")

        self.gridLayout_7.addWidget(self.N_Lbl, 6, 1, 1, 1)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 13, 1, 1, 1)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 12, 0, 1, 1)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line, 12, 1, 1, 1)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 22, 1, 1, 1)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 10, 0, 1, 1)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 24, 0, 1, 1)

        self.G_Lbl = QLabel(self.frame_4)
        self.G_Lbl.setObjectName(u"G_Lbl")

        self.gridLayout_7.addWidget(self.G_Lbl, 8, 1, 1, 1)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 21, 1, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 19, 0, 1, 1)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 20, 1, 1, 1)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 23, 0, 1, 1)

        self.k_Lbl = QLabel(self.frame_4)
        self.k_Lbl.setObjectName(u"k_Lbl")

        self.gridLayout_7.addWidget(self.k_Lbl, 2, 1, 1, 1)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 6, 0, 1, 1)

        self.sas_Lbl = QLabel(self.frame_4)
        self.sas_Lbl.setObjectName(u"sas_Lbl")

        self.gridLayout_7.addWidget(self.sas_Lbl, 10, 1, 1, 1)

        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 24, 1, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 20, 0, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 18, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 25, 1, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 17, 0, 1, 1)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 19, 1, 1, 1)

        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 23, 1, 1, 1)

        self.n_Lbl = QLabel(self.frame_4)
        self.n_Lbl.setObjectName(u"n_Lbl")

        self.gridLayout_7.addWidget(self.n_Lbl, 4, 1, 1, 1)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 21, 0, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 8, 0, 1, 1)

        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 11, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.tab_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.gridLayout_8 = QGridLayout(self.frame_6)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_8)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 5)
        self.anova_Tbl = QTableWidget(self.frame_8)
        self.anova_Tbl.setObjectName(u"anova_Tbl")
        self.anova_Tbl.setMinimumSize(QSize(0, 150))
        self.anova_Tbl.setFrameShadow(QFrame.Plain)
        self.anova_Tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.anova_Tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.anova_Tbl, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formulaTable_Lbl = QLabel(self.frame_7)
        self.formulaTable_Lbl.setObjectName(u"formulaTable_Lbl")
        self.formulaTable_Lbl.setMinimumSize(QSize(480, 135))
        self.formulaTable_Lbl.setMaximumSize(QSize(480, 135))
        self.formulaTable_Lbl.setScaledContents(True)

        self.gridLayout.addWidget(self.formulaTable_Lbl, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_7, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.acronymMeaning_Lbl = QLabel(self.frame_9)
        self.acronymMeaning_Lbl.setObjectName(u"acronymMeaning_Lbl")
        self.acronymMeaning_Lbl.setMinimumSize(QSize(257, 342))
        self.acronymMeaning_Lbl.setMaximumSize(QSize(257, 342))
        self.acronymMeaning_Lbl.setScaledContents(True)

        self.gridLayout_11.addWidget(self.acronymMeaning_Lbl, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_9, 2, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_8, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_6, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.reset_Btn.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"One-Way ANOVA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of treatment conditions (column):", None))
        self.reset_Btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.generate_Btn.setText(QCoreApplication.translate("MainWindow", u"Generate Table", None))
        self.compute_Btn.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of scores in each treatment (row):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Header Labels (separated by commas):", None))
        self.header_Ledit.setInputMask("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Raw Data Table", None))
        ___qtablewidgetitem = self.summary_Tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Treatments", None));
        ___qtablewidgetitem1 = self.summary_Tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T", None));
        ___qtablewidgetitem2 = self.summary_Tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"M", None));
        ___qtablewidgetitem3 = self.summary_Tbl.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T\u00b2", None));
        ___qtablewidgetitem4 = self.summary_Tbl.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SS", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"T =", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"n =", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"number of treatment conditions", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"number of scores in each treatment", None))
        self.N_Lbl.setText("")
        self.label_22.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"k=", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"total for each treatment condition", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u2211T\u00b2 = ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"SS =", None))
        self.G_Lbl.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"sum of all squares", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"N =", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"sum of all scores", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"M =", None))
        self.k_Lbl.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"N =", None))
        self.sas_Lbl.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"sum of squares", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G =", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"n =", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"k=", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"total number of scores", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"mean of each treatment", None))
        self.n_Lbl.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u2211T\u00b2 = ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"G =", None))
        self.label_26.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Summary", None))
        self.formulaTable_Lbl.setText("")
        self.acronymMeaning_Lbl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Anova Table", None))
    # retranslateUi

