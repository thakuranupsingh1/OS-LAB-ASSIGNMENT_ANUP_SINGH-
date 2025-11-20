import os

pid = input("Enter PID: ")

print("Process info:")
os.system(f"ps -p {pid} -o pid,ppid,state,comm")

print("\nOpen files:")
os.system(f"lsof -p {pid}")
