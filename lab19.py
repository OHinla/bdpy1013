from lab10 import courses
from pprint import pprint
from functools import reduce

pprint(courses)


def reducer(acc, v):
    acc.setdefault(v.field, [])
    acc[v.field].append(v.name)
    return acc


courseByCategory = reduce(reducer, courses, {})
pprint(courseByCategory)