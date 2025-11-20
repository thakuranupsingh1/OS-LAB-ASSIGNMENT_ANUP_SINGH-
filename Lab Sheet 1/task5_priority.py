import os, time

for i in range(3):
    pid = os.fork()
    if pid == 0:
        os.nice(i*5)
        print("Child", os.getpid(), "with nice value", i*5)
        for j in range(10000000):
            x = j*j
        print("Child", os.getpid(), "done")
        os._exit(0)

for i in range(3):
    os.wait()
print("Parent finished")
