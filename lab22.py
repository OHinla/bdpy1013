from lab10 import courses
from pprint import pprint
from functools import reduce

pprint(courses)

courseByCategory = reduce(lambda acc, v: {**acc, **{v.field: acc[v.field] + [v.name]}},
                          courses,
                          {'python': [], 'android': [], 'ccpp': []})
print(courseByCategory)