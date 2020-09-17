"""
创建Excel文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    ["学号", "姓名", "性别", "电话"],
    ["1001", '白元芳', '男', '131'],
    ["1002", '白洁', '女', '113']
]
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:D5")  #bug fix ref should be smaller

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
sheet.title = "test"
workbook.save('./res/全班学生数据.xlsx')
