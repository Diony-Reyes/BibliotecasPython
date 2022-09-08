from functools import reduce

numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sumreduce(acc, cur):
    return acc + cur


oddsum = reduce(sumreduce, filter(lambda x: x % 2 != 0, numberslist))
print(oddsum)
