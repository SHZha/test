#-*- coding:utf-8 -*-


def fib(max):
    #==========
    #函数说明：生成裴波纳契数列
    #参数说明：max:裴波纳契数列个数上限
    #==========
    n,a,b = 0,0,1
    while n <= max:
        yield b
        a,b = b,a+b
        n += 1
    return 'done'

if __name__ == '__main__':
    x = fib(20)
    while True:
        try:
            y = next(x)
            print(y,)
        except StopIteration as e:
            print('返回值:',e.value,)
            break