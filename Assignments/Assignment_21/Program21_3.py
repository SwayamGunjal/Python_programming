import threading

Count = 0
lobj = threading.Lock()

def fun1():
    global Count

    for i in range(20000):
        Count = Count + 1
    

def fun2():
    global Count

    for i in range(20000):
        Count = Count + 1
    

def fun3():
    global Count

    for i in range(20000):
        Count = Count + 1
    

def fun4():
    global Count

    for i in range(20000):
        Count = Count + 1

def fun5():
    global Count

    for i in range(20000):
        Count = Count + 1

def fun6():
    global Count

    for i in range(20000):
        Count = Count + 1

def fun7():
    global Count

    for i in range(20000):
        Count = Count + 1

def fun8():
    global Count

    for i in range(20000):
        Count = Count + 1
    

def main():


    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t3 = threading.Thread(target=fun3)
    t4 = threading.Thread(target=fun4)
    t5 = threading.Thread(target=fun5)
    t6 = threading.Thread(target=fun6)
    t7 = threading.Thread(target=fun7)
    t8 = threading.Thread(target=fun8)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    print(Count)

if __name__ == "__main__":
    main()


# -------------------------------------------------------------------------------------------------------------------- #
# Key observation : I initially tried to run it on 4 threads without the lock hoping to meet the race condition,       #
#                   but because of CPython uses the GIL, Python bytecode did not execute in parallel, masking the      #
#                   race condition. Thus i was unable to practically see the race condition occuring.                  #
#                   Then i added the rest of the 4 threads in an attempt to overload the scheduler                     #
#                   into hitting the race condition again but it still didn't hit it.                                  #
# -------------------------------------------------------------------------------------------------------------------- #
# Learnings       : 1. After some digging on the web, i found out the clever architecture of CPython and it having     #
#                      GIL, unlike its other varients such as IronPython and Jython.                                   #
#                      ----------------------------------------------------------------------------------------------- #
#                   2. I learned that GIL executes 1 thread at a time which ultimately prevents race condition         #
#                      from occuring but sometimes when it switches after a fixed number of bytecode instructions      #
#                      or during blocking operations (I/O, sleep, etc.)                                                #
#                      ----------------------------------------------------------------------------------------------- #
#                   3. I learned that, it can hit the race conditions on a different hardware containing less cores.   #
#                      ----------------------------------------------------------------------------------------------- #
#                   4. And it can hit the race condition on other varients of python such as Jython, IronPython.       #
# -------------------------------------------------------------------------------------------------------------------- #
# Key takeaway    : Even though it didn't hit the race condition on my hardware doesn't mean it won't hit on a         #
#                   different hardware having less cores or another varient of python(Jython, IronPython,etc).         #
#                   Which is exactly the reason why we need to lock the threads to avoid the race condition as         #
#                   the same code becomes platform dependent if the lock is not enabled.                               #
# -------------------------------------------------------------------------------------------------------------------- #
