from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws=wb.active

ws.delete_rows(8)

ws.delete_rows(2, 2)

ws.delete_cols(1)

ws.delete_cols(5,2)

wb.save("sample_delete_row.xlsx")