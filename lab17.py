from lab10 import courses
from lab16 import incomes
from functools import reduce
from pprint import pprint

if __name__ == '__main__':
    pprint(courses)
    total = reduce((lambda result, e: result + e['income']), incomes, 0)
    print('by reduce', total)
    sum = sum(e['income'] for e in incomes)
    print('by python sum', sum)
    maxIncome = reduce((lambda result, e: max(result, e['income'])), incomes, 0)
    print(maxIncome)
    minIncome = reduce((lambda r, e: min(r, e['income'])), incomes, 99999999)
    print(minIncome)