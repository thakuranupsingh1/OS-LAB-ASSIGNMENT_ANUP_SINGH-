# task2.py - simulate system startup using processes + logging

import multiprocessing
import logging
import time

logging.basicConfig(
    filename='system_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

def process_task(name):
    logging.info(f"{name} started")
    time.sleep(2)
    logging.info(f"{name} terminated")

if __name__ == '__main__':
    print("System Booting...")

    p1 = multiprocessing.Process(target=process_task, args=("Process-1",), name="Process-1")
    p2 = multiprocessing.Process(target=process_task, args=("Process-2",), name="Process-2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("System Shutdown.")
