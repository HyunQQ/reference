# 참고 >
# https://hamait.tistory.com/834
# https://soooprmx.com/archives/5622
########### generator ################
def simple_gen():
    yield "Hello"
    yield "World"


gen = simple_gen()
print(next(gen))
print(next(gen))

########## coroutines ############
def coro():
    hello = yield "Hello"
    yield hello


c = coro()
print(next(c))
print(c.send("World"))


