import pandas as pd
class ExcelService:
    def load_excel(self,path):
        return pd.read_excel(path)
    def detect_columns(self, cols):
        r={"date":"","amount":"","account":""}
        for c in cols:
            s=str(c)
            l=s.lower()
            if "تاریخ" in s or "date" in l: r["date"]=s
            if "مبلغ" in s or "amount" in l: r["amount"]=s
            if "حساب" in s or "account" in l: r["account"]=s
        return r
