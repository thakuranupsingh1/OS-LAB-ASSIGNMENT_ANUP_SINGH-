import os

n = 3
for i in range(n):
    pid = os.fork()
    if pid == 0:
        print("Child PID:", os.getpid(), "Parent PID:", os.getppid(), "Message: Hello from child", i+1)
        os._exit(0)

for i in range(n):
    os.wait()
print("Parent process finished:", os.getpid())
