from lab10 import courses
from pprint import pprint
from itertools import groupby

pprint(courses)
courses = sorted(courses, key=lambda c: c.field)
pprint(courses)
coursesByCategory = {c[0]: list(c[1]) for c in groupby(courses, key=lambda c: c.field)}
pprint(coursesByCategory)