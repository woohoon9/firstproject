from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws=wb.active

ws.insert_rows(8)

ws.insert_rows(3, 4)

ws.insert_cols(2)

ws.insert_cols(0, 2)

wb.save("sample_insert_rows.xlsx")