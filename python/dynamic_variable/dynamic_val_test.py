#동적 변수 만들기
for i in range(10):
    globals()['variable{}'.format(i)] = [x for x in range(3)]


print(variable1)
print(variable2)
