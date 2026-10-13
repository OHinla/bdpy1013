from pprint import pprint
courses = [
    {'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
    {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
    {'name': 'andbiz3', 'field': 'android', 'attendee': 5, 'remote': False},
]
pprint(courses)
courses[0]['name']="PLGBT"
pprint(courses) # mutable
