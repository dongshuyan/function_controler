import time
from function_controler.func_ctrl import func_ctrl

def a2():
    print("开始执行a2")
    time.sleep(1)
    print("执行完成")
    a=2
    return a


def a3(a,b):
    print("开始执行a3")
    time.sleep(3)
    print("执行完成a3")
    return a+b


def a4(a,b):
    print("开始执行a4")
    for i in range(5):
        print(i)
        time.sleep(1)
    print("执行完成a4")
    return a+b

a=func_ctrl(func=a2,limit_time=0.5)
print(a,end='\n\n')
a=func_ctrl(func=a2,limit_time=2)
print(a,end='\n\n')

a=func_ctrl(func=a3,args=(1,2),limit_time=2,allow_log=False)
print(a,end='\n\n')
a=func_ctrl(func=a3,args=(1,2),limit_time=4,allow_log=False)
print(a,end='\n\n')

a=func_ctrl(func=a4,args=(1,2),limit_time=2,kill=False)
print(a,end='\n\n')
a=func_ctrl(func=a4,args=(1,2),limit_time=2,kill=False,allow_log=False)
print(a,end='\n\n')
a=func_ctrl(func=a4,args=(1,2),limit_time=0,kill=False,allow_log=False)
print(a,end='\n\n')

a=func_ctrl(func=a4,args=(1,2),limit_time=2,kill=True,allow_log=False)
print(a,end='\n\n')
a=func_ctrl(func=a4,args=(1,2),limit_time=0,kill=True,allow_log=False)
print(a,end='\n\n')