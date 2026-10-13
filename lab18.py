from lab10 import courses
from pprint import pprint
from functools import reduce
pprint(courses)

def reducer(acc, v):
    acc[v.field].append(v.name)
    return acc
courseByCategory = reduce(reducer, courses,{'python':[], 'android':[]})
pprint(courseByCategory)