import sys

def run(args):
    print(args)
    for i in args:
        print("--------")
        print(i)

if __name__ =="__main__":
    run(sys.argv)

################################################################
# 결과
# cmd     :   python using_system_arg.py arg1 arg2
# output  :   ['anal_server_with_rabbit.py', 'arg1', 'arg2']
#             --------
#             anal_server_with_rabbit.py
#             --------
#             arg1
#             --------
#             arg2
################################################################
