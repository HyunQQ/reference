#동적 변수 만들기
for i in range(10):
    globals()['variable{}'.format(i)] = [x for x in range(3)]


print(variable1)
print(variable2)



data = ['v107_report', 'v230_report', 'v107_data', 'v230_data']

for name in data:
    globals()[name] = name.split('_')[1]
    print(globals()[name])