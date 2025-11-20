import os

commands = [["ls"], ["date"], ["ps"]]

for cmd in commands:
    pid = os.fork()
    if pid == 0:
        os.execvp(cmd[0], cmd)
    else:
        os.wait()
