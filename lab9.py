
from lab8 import course
from pprint import pprint

poop = course(name='poop', field='python', attendee=15, remote=False)
bdpy = course(name='bdpy', field='python', attendee=10, remote=True)
coursesList = [poop, bdpy]
pprint(coursesList)
del coursesList[0]
pprint(coursesList)
coursesList = [poop, bdpy]
coursesTuple = tuple(coursesList)
pprint(coursesTuple)
#del coursesTuple[0]