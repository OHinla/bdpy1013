from lab10 import courses
from pprint import pprint
from functools import reduce
import time
import multiprocessing

def transform(x):
    print(f"convert category:{x.name}")
    time.sleep(4)
    result = {'name': x.name, 'revenue': x.attendee * 5090}
    return result

if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool()
    print(f"now run with process:{pool._processes}")
    result = tuple(pool.map(transform, courses))
    end = time.time()
    pprint(result)
    print("total spent:{}".format(end - start))