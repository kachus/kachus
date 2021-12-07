
import timeit
import numpy as np
numbers  = np.array(np.random.randint(low = 1, high = 5,  size = 100000))
def test2():
    numbers_are_in_tail = []
    counter = np.bincount(numbers)
    for number in numbers:
        counter[number] -= 1
    if counter[number] >0:
        numbers_are_in_tail.append(True)
    else:
        numbers_are_in_tail.append(False)
    return numbers_are_in_tail
count = 1

times2 = timeit.timeit("test2()", setup="from __main__ import test2", number=count)
print('test2:', times2)
