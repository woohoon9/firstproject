import xlsxwriter
import datetime

workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet('Cover_Page')

expense = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50]
)

e = datetime.datetime.now()
row = 1
col = 1

for item, cost in (expense):
    worksheet.write(row, col, item)
    worksheet.write(row, col +1, cost)
    row +=1


worksheet.write(row, 1, 'Total')
worksheet.write(row, 2, '=SUM(C1:C4)')

worksheet.write('A12','Insert an image with an offset:')
worksheet.insert_image('B12', 'logo.png',{'x_offset':15, 'y_offset':10})


worksheet.write('A23', 'Insert a scaled image:')
worksheet.insert_image('B23', 'logo.png', {'x_scale': 0.2, 'y_scale': 0.2})

worksheet.write('A25', 'Current data and time = %s'%e)

workbook.close()