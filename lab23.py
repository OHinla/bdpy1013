from lab10 import courses
from pprint import pprint
from functools import reduce
import time

def transform(x):
    print(f"convert category:{x.name}")
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    return result

start = time.time()
result = tuple(map(transform, courses))
end = time.time()
pprint(result)
print("total spent:{}".format(end - start))