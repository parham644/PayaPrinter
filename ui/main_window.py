from PySide6.QtWidgets import *
from services.excel_service import ExcelService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.excel=ExcelService()
        self.setWindowTitle('Paya Printer v0.2')
        self.resize(1200,800)
        w=QWidget(); self.setCentralWidget(w)
        v=QVBoxLayout()
        self.btn=QPushButton('انتخاب فایل اکسل')
        self.btn.clicked.connect(self.open_excel)
        self.table=QTableWidget()
        self.cmb_date=QComboBox(); self.cmb_amount=QComboBox(); self.cmb_account=QComboBox()
        f=QFormLayout()
        f.addRow('تاریخ',self.cmb_date)
        f.addRow('مبلغ',self.cmb_amount)
        f.addRow('حساب',self.cmb_account)
        g=QGroupBox('تشخیص ستون ها'); g.setLayout(f)
        v.addWidget(self.btn); v.addWidget(g); v.addWidget(self.table)
        w.setLayout(v)

    def open_excel(self):
        fn,_=QFileDialog.getOpenFileName(self,'Excel','','Excel Files (*.xlsx *.xls)')
        if not fn: return
        df=self.excel.load_excel(fn)
        cols=[str(c) for c in df.columns]
        self.table.setColumnCount(len(cols))
        self.table.setRowCount(len(df))
        self.table.setHorizontalHeaderLabels(cols)
        for r in range(len(df)):
            for c in range(len(cols)):
                self.table.setItem(r,c,QTableWidgetItem(str(df.iloc[r,c])))
        for cmb in [self.cmb_date,self.cmb_amount,self.cmb_account]:
            cmb.clear(); cmb.addItems(cols)
        found=self.excel.detect_columns(cols)
        if found['date']: self.cmb_date.setCurrentText(found['date'])
        if found['amount']: self.cmb_amount.setCurrentText(found['amount'])
        if found['account']: self.cmb_account.setCurrentText(found['account'])
