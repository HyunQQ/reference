# <Title>
# openpyxl을 통해 excel 보고서 만들기

# <Install>
# pip install openpyxl

# <Using Version>
# Python 3.6.5
# pip freeze | findstr psycopg2
# openpyxl==2.5.3

# <Reference>
# doc : https://openpyxl.readthedocs.io/en/stable/


# <Example Select Code>
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, Color, GradientFill
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

file_nm = "excel-test.xlsx"

wb = Workbook()
ws_report = wb.create_sheet("Report",0)  # Qsheet1 이름의 시트를 1번째 위치에 생성
ws_data = wb.create_sheet("Data",1)  # Qsheet2 이름의 시트를 2번째 위치에 생성
# 위치를 건너뛰고 생성했을 경우 sheet이름의 중산 시트가 1개 생성되고 설정 이름의 시트가 생성된다. 
# 순서가 잘못되면 원하는 위치로 생성되지 않는 것으로 보임.
# ex)ws = wb.create_sheet("Qsheet5",5)  -> 생성시트 (Qsheet1, Qsheet2, sheet,  Qsheet5)

######################### Report sheet #########################
# cell for title 
ws_report.merge_cells('A1:F1')
ws_report['A1'] = 'Report'
title = ws_report['A1']

title.fill = PatternFill("solid", fgColor="DDDDDD")
title.font = Font(name='맑은 고딕', size = 15, bold=True)
title.alignment = Alignment(horizontal='center', vertical='center')

#################################################################


######################### Data sheet #########################
# cell for title 
ws_data.merge_cells('A1:F1')
ws_data['A1'] = 'Data'
title = ws_data['A1']

title.fill = PatternFill("solid", fgColor="DDDDDD")
title.font = Font(name='맑은 고딕', size = 15, bold=True)
title.alignment = Alignment(horizontal='center', vertical='center')

# cell for dataframe data
data = pd.DataFrame([[1,2,3],
            [4,5,6],
            [7,8,9]])

for r in dataframe_to_rows(data, index=False, header=True):
    ws_data.append(r)

###############################################################



### sheet 삭제 ###
# wb.remove_sheet(ws)


wb.save(file_nm)
wb.close()

