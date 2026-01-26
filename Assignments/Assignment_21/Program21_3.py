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


# ------------------------------------------------------------------------------------------------------------------------ #
# Key Observation : I initially attempted to observe a race condition by running multiple threads without a lock.          #
#                   However, in CPython, the Global Interpreter Lock (GIL) allows only one thread to execute Python        #
#                   bytecode at a time, which masked the race condition in my experiments. Increasing the number           #
#                   of threads did not expose the issue due to the same behavior.                                          #
# ------------------------------------------------------------------------------------------------------------------------ #
# Learnings       : 1. CPython uses a Global Interpreter Lock (GIL), unlike implementations such as Jython and IronPython. #
#                      --------------------------------------------------------------------------------------------------- #
#                   2. The GIL reduces the likelihood of race conditions by serializing bytecode execution, but it does    #
#                       not eliminate them.                                                                                #
#                      --------------------------------------------------------------------------------------------------- #
#                   3. Race conditions depend on scheduling and interpreter behavior rather than hardware core count.      #
#                      --------------------------------------------------------------------------------------------------- #
#                   4. Python implementations without a GIL (Jython, IronPython) can expose race conditions more easily.   #
# ------------------------------------------------------------------------------------------------------------------------ #
# Key Takeaway    : Even if a race condition is not practically observable on a specific platform or interpreter,          #
#                   the code is still logically unsafe. Therefore, explicit locking is required to ensure correct,         #
#                   portable, and platform-independent behavior.                                                           #
# ------------------------------------------------------------------------------------------------------------------------ #