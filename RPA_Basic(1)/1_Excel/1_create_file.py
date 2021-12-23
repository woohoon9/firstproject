from openpyxl import Workbook
wb=Workbook()
ws = wb.active 
ws.title ="Nadosheet"
wb.save("sample.xlsx")
wb.close
