import sys
from assets.ui_AnovaOneWay import Ui_MainWindow
from assets import util
from PySide2.QtWidgets import QMainWindow, QApplication, QItemDelegate, QLineEdit
from PySide2.QtGui import QDoubleValidator, QPixmap
from PySide2.QtCore import QSize

class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        
        self.UI.generate_Btn.clicked.connect(self.generateTable)
        self.UI.compute_Btn.clicked.connect(self.compute)
        self.UI.reset_Btn.clicked.connect(self.reset)
        
        self.UI.anova_Tbl.setColumnCount(5)
        self.UI.anova_Tbl.setHorizontalHeaderLabels(['SS', 'df', 'MS', 'F', 'p'])
        self.UI.anova_Tbl.setRowCount(3)
        self.UI.anova_Tbl.setVerticalHeaderLabels(['Treatment (Between) ', 'Error (Within) ', 'Total'])
        
        self.UI.rawData_Tbl.setItemDelegate(inputValidator())
        
        self.UI.acronymMeaning_Lbl.setMinimumSize(QSize(257, 342))
        self.UI.acronymMeaning_Lbl.setMaximumSize(QSize(257, 342))
        self.UI.acronymMeaning_Lbl.setPixmap(QPixmap(u"assets/acronymMeaning.jpeg"))
        self.UI.acronymMeaning_Lbl.setScaledContents(True)
        
        self.UI.formulaTable_Lbl.setMinimumSize(QSize(480, 135))
        self.UI.formulaTable_Lbl.setMaximumSize(QSize(480, 135))
        self.UI.formulaTable_Lbl.setPixmap(QPixmap(u"assets/formulaTable.jpeg"))
        self.UI.formulaTable_Lbl.setScaledContents(True)
        
        self.show()
        
    def generateTable(self):
        column = self.UI.column_Sbox.value()
        row = self.UI.row_Sbox.value()
        
        self.UI.rawData_Tbl.setColumnCount(column)
        self.UI.rawData_Tbl.setRowCount(row)
        
        treatments = self.UI.header_Ledit.text()
        
        header = []
        if treatments:
            header = treatments.split(",")
        else:
            for i in range(1, column+1):
                header.append(str(i))
               
        self.UI.rawData_Tbl.setHorizontalHeaderLabels(header)
        
    def compute(self):
        util.oneWayAnova(self.UI)

    def reset(self):
        self.UI.header_Ledit.setText("")
        self.UI.row_Sbox.setValue(0)
        self.UI.column_Sbox.setValue(0)
        
        self.UI.rawData_Tbl.setRowCount(0)
        self.UI.rawData_Tbl.setColumnCount(0)
        
        self.UI.anova_Tbl.setRowCount(0)
        self.UI.anova_Tbl.setColumnCount(0)
        
        self.UI.summary_Tbl.setRowCount(0)
        self.UI.anova_Tbl.setRowCount(0)
        
        self.UI.k_Lbl.setText("")
        self.UI.n_Lbl.setText("")
        self.UI.N_Lbl.setText("")
        self.UI.G_Lbl.setText("")
        self.UI.sas_Lbl.setText("")
        
class inputValidator(QItemDelegate):
    def createEditor(self, parent, option, index):
        data_Ledit = QLineEdit(parent)
        data_Ledit.setValidator(QDoubleValidator())
        return data_Ledit

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(application.exec_())