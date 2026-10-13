
from lab10 import courses
from pprint import pprint
from functools import reduce
from collections import defaultdict

pprint(courses)


def reducer(acc, v):
    # acc.setdefault(v.field, [])
    acc[v.field].append(v.name)
    return acc


courseByCategory = dict(reduce(reducer, courses, defaultdict(list)))
pprint(courseByCategory)