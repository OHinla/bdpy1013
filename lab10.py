from lab8 import course
from pprint import pprint

poop = course(name='poop', field='python', attendee=15, remote=False)
bdpy = course(name='bdpy', field='python', attendee=10, remote=True)
pykt = course(name='pykt', field='python', attendee=9, remote=True)
andbiz = course(name='andbiz', field='android', attendee=5, remote=True)
aiocv = course(name='aiocv', field='python', attendee=10, remote=False)
courses = (poop, bdpy, pykt, andbiz, aiocv)

if __name__ == '__main__':
    pprint(courses)
    remoteCourses = filter(lambda x: x.remote is True, courses)
    pprint(remoteCourses)
    pprint([x for x in remoteCourses])
    highBonusCourses = filter(lambda x: x.attendee < 10, courses)
    pprint([x for x in highBonusCourses])