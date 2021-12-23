import clr
import datacompy
import pandas as pd
import xlrd

loc1 = ("C:\Wooswork\02. Automation Estimating\03_Lots Sample\Dynamo Python Scripts\Test\Change detection\Change Dectection V01")
loc2 = ("C:\Wooswork\02. Automation Estimating\03_Lots Sample\Dynamo Python Scripts\Test\Change detection\Change Dectection V02-test")

wb1 = xlrd.open_workbook(loc1)
wb2 = xlrd.open_workbook(loc2)

sheet1 = wb1.sheet_by_name('01.EST_Doors')
sheet2 = wb2.sheet_by_name('01.EST_Doors')

print(sheet1.cell_value())
print(sheet2.cell_value())
