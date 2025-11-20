import os, time

pid = os.fork()
if pid > 0:
    print("For Zombie: parent not waiting, child may be zombie")
    time.sleep(5)
elif pid == 0:
    print("Child running, exiting immediately")
    os._exit(0)

time.sleep(2)

pid2 = os.fork()
if pid2 == 0:
    print("For Orphan: child running, parent exits early")
    time.sleep(6)
    print("Child finished:", os.getpid())
else:
    print("Parent exiting before orphan child ends")
    os._exit(0)
