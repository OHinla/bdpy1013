from collections import namedtuple

from lab10 import courses
from pprint import pprint

courseSummary = namedtuple('courseSummary', ['name', 'field'])
nameAndField = map(lambda x: courseSummary(name=x.name, field=x.field), courses)
pprint(tuple(nameAndField))