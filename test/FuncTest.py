import itertools


class_cycle = itertools.cycle([1,2,3,4])
print(class_cycle)

for each in itertools.cycle(class_cycle):
    print(each)