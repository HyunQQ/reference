# html tag가 들어 있는 text를 정규식을 이용해 정재

import re

text = '<p style="text-align: center;"><font color="#000000" style="background-color: rgb(255, 255, 0);">test</font></p><ol><li><font color="#000000"><span style="background-color: rgb(255, 255, 0);">summer note test</span></font></li><li><font color="#000000"><span style="background-color: rgb(255, 255, 0);">2</span></font></li><li><font color="#000000"><span style="background-color: rgb(255, 255, 0);">3</span></font></li><li><font color="#000000"><span style="background-color: rgb(255, 255, 0);">4</span></font></li></ol><p><h1><b><span style="font-family: &quot;Arial Black&quot;;">test 문자 입력중</span></b></h1></p><p><br></p>'

result = re.sub(r'<.*?>', '',text)
print(result)