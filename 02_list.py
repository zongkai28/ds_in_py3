# python 3.7.3
from timeit import Timer

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li += [i]

def t3():
    li = []
    for i in range(10000):
        li = li + [i]

def t4():
    li = [i for i in range(10000)]

def t5():
    li = list(range(10000))

def t6():
    li = []
    for i in range(10000):
        li.extend([i])

def t7():
    li = []
    for i in range(10000):
        li.insert(0, i)

timer1 = Timer("t1()", "from __main__ import t1")
print("append:", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("+=:", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("+:", timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("[i for i in range)]:", timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("list(range()):", timer5.timeit(1000))

timer6 = Timer("t6()", "from __main__ import t6")
print("extend():", timer6.timeit(1000))

timer7 = Timer("t7()", "from __main__ import t7")
print("insert(0):", timer7.timeit(1000))