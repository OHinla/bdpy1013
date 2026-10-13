from lab10 import courses
from pprint import pprint

pprint([x for x in courses])
pprint(tuple([x for x in courses]))
pprint(tuple(x for x in courses))
print("Python課:")
pprint(tuple(x for x in courses if x.field == 'python'))
print("遠距課:")
pprint(tuple(x for x in courses if x.remote == True))

print("Python遠距課:")
pprint(tuple(x for x in courses if (x.remote == True and x.field == 'python')))

from lab10 import courses
from pprint import pprint

nameAndField = map(lambda x: {'name': x.name, 'field': x.field}, courses)
pprint(tuple(nameAndField))
nameAndFieldTuple = tuple(map(lambda x: {'name': x.name, 'field': x.field}, courses))
nameAndFieldTuple[0]['name'] = "XXXXX"
pprint(nameAndFieldTuple)