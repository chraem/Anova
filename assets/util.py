from PySide2.QtWidgets import QTableWidgetItem
from scipy import stats

dataFrame = {}

def oneWayAnova(UI):
    getRawData(UI.rawData_Tbl)
    anova(UI)

def getRawData(rawData_Tbl):
    rows = rawData_Tbl.rowCount()
    cols = rawData_Tbl.columnCount()
    
    for col in range(cols):
        key = rawData_Tbl.horizontalHeaderItem(col).text()
        dataFrame[key] = []
        
        for row in range(rows):
            data = rawData_Tbl.item(row, col)
            if data:
                dataFrame[key].append(float(rawData_Tbl.item(row, col).text()))
            else:
                rawData_Tbl.setItem(row, col, QTableWidgetItem("0"))
                dataFrame[key].append(0.0)

    return dataFrame
            
def anova(UI):
    treatments = list(dataFrame.keys())
    k = float(UI.column_Sbox.value())
    n = float(UI.row_Sbox.value())
    UI.summary_Tbl.setRowCount(len(treatments))
    G = 0.0
    total_SS = 0.0
    ssWithin = 0.0
    
    # ============================================
    # Computations
    N = n*k
    for row, treatment in enumerate(treatments):
        total = 0.0
        M = 0.0
        Tsqr = 0.0
        SS = 0.0
        
        
        for score in dataFrame[treatment]:
            total = total + score
            G = G + score

            Tsqr = Tsqr + (score ** 2)
        
        M = total / len(dataFrame[treatment])
        SS = Tsqr - ((total**2)/n)
        ssWithin = ssWithin + SS
        total_SS = total_SS + Tsqr
    # ============================================
        
        # Treatments Column
        UI.summary_Tbl.setItem(row, 0, QTableWidgetItem(treatment))
        # T(total for each treatment condition) Column
        UI.summary_Tbl.setItem(row, 1, QTableWidgetItem(str(total)))
        # M(mean of each treatment condition) Column
        UI.summary_Tbl.setItem(row, 2, QTableWidgetItem(str(M)))
        # T^2 Column
        UI.summary_Tbl.setItem(row, 3, QTableWidgetItem(str(Tsqr)))
        # SS Column
        UI.summary_Tbl.setItem(row, 4, QTableWidgetItem(str(SS)))
        
    
    # Summary on the side
    UI.k_Lbl.setText(str(k))
    UI.n_Lbl.setText(str(n))
    UI.N_Lbl.setText(str(N))
    UI.G_Lbl.setText(str(G))
    UI.sas_Lbl.setText(str(total_SS))
    
    # Anova Table
    ssTotal = total_SS - (G**2/N)
    ssBetween = ssTotal - ssWithin
    
    UI.anova_Tbl.setItem(0,0, QTableWidgetItem(str(ssBetween)))
    UI.anova_Tbl.setItem(1,0, QTableWidgetItem(str(ssWithin)))
    UI.anova_Tbl.setItem(2,0, QTableWidgetItem(str(ssTotal)))
    
    dfTotal = N - 1
    dfWithin = N - k
    dfBetween = k - 1
    
    UI.anova_Tbl.setItem(0,1, QTableWidgetItem(str(dfBetween)))
    UI.anova_Tbl.setItem(1,1, QTableWidgetItem(str(dfWithin)))
    UI.anova_Tbl.setItem(2,1, QTableWidgetItem(str(dfTotal)))
    
    msBetween = ssBetween / dfBetween
    msWithin = ssWithin / dfWithin
    
    UI.anova_Tbl.setItem(0,2, QTableWidgetItem(str(msBetween)))
    UI.anova_Tbl.setItem(1,2, QTableWidgetItem(str(msWithin)))
    
    dataList = []
    for key in dataFrame.keys():
        dataList.append(dataFrame[key])
        
    fValue, pValue = stats.f_oneway(*dataList)    
    UI.anova_Tbl.setItem(0,3, QTableWidgetItem(str(fValue)))
    UI.anova_Tbl.setItem(0,4, QTableWidgetItem(str(pValue)))
    