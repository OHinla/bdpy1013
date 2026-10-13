from lab10 import courses
from pprint import pprint
import time
import os
from concurrent.futures import ProcessPoolExecutor


def transform(x):
    print(f"convert category:{x.name} with id {os.getpid()}")
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"convert finished category:{x.name} with id {os.getpid()}")
    return result


if __name__ == '__main__':
    start = time.time()
    with ProcessPoolExecutor(max_workers=3) as pool:
        result = tuple(pool.map(transform, courses))
    end = time.time()
    pprint(result)
    print("total spent:{}".format(end - start))