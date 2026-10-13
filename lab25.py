from lab10 import courses
from pprint import pprint
from functools import reduce
import time
import multiprocessing
import os


def transform(x):
    print(f"convert category:{x.name} with id {os.getpid()}")
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"convert finished category:{x.name} with id {os.getpid()}")
    return result


if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(processes=2, maxtasksperchild=2)
    print(f"now run with process:{pool._processes}")
    result = tuple(pool.map(transform, courses))
    end = time.time()
    pprint(result)
    print("total spent:{}".format(end - start))