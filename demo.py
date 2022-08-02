import time
from function_controler.func_ctrl import func_ctrl

def a2():
    print("A2 Start")
    time.sleep(1)
    print("A2 Finished")
    a=2
    return a


def a3(a,b):
    print("A3 Start")
    time.sleep(3)
    print("A3 Finished")
    return a+b


def a4(a,b):
    print("A4 Start")
    for i in range(5):
        print(i)
        time.sleep(1)
    print("A4 Finished")
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