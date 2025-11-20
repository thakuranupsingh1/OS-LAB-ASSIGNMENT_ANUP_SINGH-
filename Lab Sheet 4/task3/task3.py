# task3.py - IPC using fork() + pipe() (fallback for Windows)

import os
import sys

def unix_pipe_example():
    r, w = os.pipe()
    pid = os.fork()

    if pid > 0:
        os.close(r)
        os.write(w, b"Hello from parent")
        os.close(w)
        os.wait()
    else:
        os.close(w)
        msg = os.read(r, 1024)
        os.close(r)
        print("Child received:", msg.decode())
        os._exit(0)

def fallback_pipe():
    from multiprocessing import Process, Pipe

    def child(conn):
        msg = conn.recv()
        print("Child received (fallback):", msg)
        conn.close()

    pconn, cconn = Pipe()
    p = Process(target=child, args=(cconn,))
    p.start()
    pconn.send("Hello from parent (multiprocessing)")
    pconn.close()
    p.join()

if __name__ == "__main__":
    if hasattr(os, "fork"):
        unix_pipe_example()
    else:
        fallback_pipe()
