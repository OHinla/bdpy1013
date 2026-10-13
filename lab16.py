from collections import namedtuple

from lab10 import courses
from pprint import pprint

incomes = [{'name': c.name, 'income': c.attendee * 8000} for c in courses]
if __name__ == '__main__':
    pprint(incomes)
    pprint(tuple(incomes))
    pprint(tuple((d.name, d.attendee * 8000) for d in courses))