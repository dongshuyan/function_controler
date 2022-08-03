import time
import threading
from loguru import logger
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id 无效的线程ID")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed 结束线程失败")

class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        """
        why: 因为threading类没有返回值,因此在此处重新定义MyThread类,使线程拥有返回值
        """
        super(MyThread, self).__init__()
        self.func = target
        self.args = args
    def run(self):
        # 接受返回值
        self.result = self.func(*self.args)
    def get_result(self):
        # 线程不结束,返回值为None
        try:
            return self.result
        except Exception:
            return None
    def kill(self): 
        _async_raise(self.ident, SystemExit)
        return None


# 为了限制真实请求时间或函数执行时间的装饰器
def limit_decor(limit_time,kill=True):
    """
    :param limit_time: 设置最大允许执行时长,单位:秒 如果设置0则没有限制
    :return: 未超时返回被装饰函数返回值,超时则返回 None
    """
    def functions(func):
        # 执行操作
        def run(*params):
            
            thre_func = MyThread(target=func, args=params)
            # 主线程结束(超出时长),则线程方法结束
            thre_func.setDaemon(True)
            thre_func.start()
            #limit_time如果<0 就不限制
            if limit_time<1e-9:
                thre_func.join()
                return thre_func.get_result()

            # 计算分段沉睡次数
            sleep_num = int(limit_time // 1)
            sleep_nums = round(limit_time % 1, 1)
            # 多次短暂沉睡并尝试获取返回值
            for i in range(sleep_num):
                time.sleep(1)
                infor = thre_func.get_result()
                if infor:
                    return infor
            time.sleep(sleep_nums)
            # 最终返回值(不论线程是否已结束)
            if thre_func.get_result():
                return thre_func.get_result()
            else:
                if kill:
                    thre_func.kill()
                return"Func_Ctrl_TimeOut"  #超时返回

        return run

    return functions


def func_maxtime(func,args=(),limit_time=0,kill=True,allow_log=True):
    """
    :param 
        func:被限制运行时长的函数
        args:此函数的参数
        limit_time: 设置最大允许执行时长,单位:秒 如果设置0则没有限制
        kill:超时之后是否结束线程
        allow_log:是否允许打印日志
    :return: 未超时返回被装饰函数返回值,超时则返回 None
    """
    @limit_decor(limit_time,kill)
    def temp_func(args):
        return args[0](*args[1])
    if allow_log:
        logger.info('Start running '+func.__name__+'')
    temp=(func,args)
    a_theadiing = MyThread(target=temp_func,args=(temp,))
    a_theadiing.start()
    a_theadiing.join()
    a = a_theadiing.get_result()
    if a=='Func_Ctrl_TimeOut':
        if allow_log:
            logger.warning('Running '+func.__name__+' TimeOut')
        return None
    else:
        if allow_log:
            logger.info('finish running '+func.__name__+'')
    return a

def main():
    print('Usage:\nfunc_maxtime(func=FUNCTION_NAME,args=(ARGS),limit_time=LIMIT_TIME,kill=BOOL,allow_log=BOOL) ')
