import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

if __name__ == '__main__':
    print(type(course))
    poop = course(name='poop', field='python', attendee=15, remote=True)
    print(poop)
    poop.name = "POOP"