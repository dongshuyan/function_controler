# function_controler
Control the maximum running time of a function.

# parameters
## func
Functions that are limited in runtime, type: function  
被限制运行时长的函数, type: function  
## args
Parameters of func, type: tuple, defeat: args=()  
此函数的参数, type: tuple, defeat:args=()  
## limit_time
The maximum execution time in seconds. If you set 0, there is no limit, type: float, defeat: limit_time=0  
设置最大允许执行时长,单位:秒 如果设置0则没有限制, type: float, defeat: limit_time=0  
## kill
Whether to stop the thread after the timeout, type: bool, defeat: kill=True  
超时之后是否结束线程, type: bool, defeat: kill=True  
## allow_log
Whether to print the logs, type: bool, defeat: allow_log=True  
是否允许打印日志, type: bool, defeat: allow_log=True  

# Return
Return the return value of func,return None if timeout  
未超时返回被装饰函数返回值,超时则返回 None  

# Useage
from function_controler.func_ctrl import func_ctrl  
func_ctrl(func=FUNCTION_NAME,args=(ARGS),limit_time=LIMIT_TIME,kill=BOOL,allow_log=BOOL)  
![Img_Demo](https://ptpimg.me/9dlu9f.png)
  
See [demo.py](https://github.com/dongshuyan/function_controler/blob/main/demo.py) for details  

# Reference
[Python控制函数运行时间](https://www.cnblogs.com/lyxdw/p/10033118.html)  
