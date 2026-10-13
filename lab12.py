from lab10 import courses
from pprint import pprint


def available(c):
    return c.attendee >= 8


def isRemote(c):
    return c.remote is True


print("目前會開的課")
pprint(tuple(filter(available, courses)))
print("遠距課")
pprint(tuple(filter(isRemote, courses)))
print("遠距目前會開的課")
pprint(tuple(filter(isRemote, filter(available, courses))))
print("遠距目前會開的課-2")
pprint(tuple(filter(available, filter(isRemote, courses))))