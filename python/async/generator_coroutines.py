# python의 stack frame은 메모리의 stack 영역에 올라가는 것이 아니라, heap 영역에 할당된다. 
# 따라서 generator가 실행을 일시정지하고 값을 return 할 때 stack frame을 유지할 수 있다. 
# yield를 만나는 순간, 해단 stack frame과 코드를 어디서부터 ㅈ재개할지에 대한 정보를 보관하는 것이다.  
# 이런 특징을 이용해서 coroutine을 구현하였다.

# 참고 >
# https://hamait.tistory.com/834
# https://soooprmx.com/archives/5622
# https://hwangheek.github.io/2019/asynchronous-python/
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


