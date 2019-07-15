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
from openpyxl.styles import Font, Alignment
import numpy as np

file_nm = "excel-test.xlsx"

wb = Workbook()
ws = wb.create_sheet("Qsheet1",0)  # Qsheet1 이름의 시트를 1번째 위치에 생성
ws2 = wb.create_sheet("Qsheet2",1)  # Qsheet2 이름의 시트를 2번째 위치에 생성
# 위치를 건너뛰고 생성했을 경우 sheet이름의 중산 시트가 1개 생성되고 설정 이름의 시트가 생성된다. 
# 순서가 잘못되면 원하는 위치로 생성되지 않는 것으로 보임.
# ex)ws = wb.create_sheet("Qsheet5",5)  -> 생성시트 (Qsheet1, Qsheet2, sheet,  Qsheet5)

# test_data = np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])

# print(test_data.shape)

# for row_index in range 

# cell 작업
ws.merge_cells('B2:F2')
ws['B2'] = '분석 결과'



# sheet 삭제
# wb.remove_sheet(ws)
# wb.save(file_nm)

