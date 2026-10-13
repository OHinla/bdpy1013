from lab10 import courses
from pprint import pprint

pprint(tuple(filter(lambda x: x.remote is True, courses)))
pprint(tuple(filter(lambda x: True, courses)))
pprint(tuple(filter(lambda x: False, courses)))
pprint(tuple(filter(lambda x: x.attendee < 10, courses)))