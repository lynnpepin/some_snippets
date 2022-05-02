'''countsort.py

This is example code to show how this works

In computer science, we deal with real or integer numbers.
But in programming, we deal with floats or ints.
These are finite sets, which means we can apply counting sort,
which runs in Θ(k + n) time and space.

Realistically, it is only useful for small K, such as when
working with 8-bit or 16-bit floats or ints.

Let's sort numbers uint8, i.e. integers in the range [0, 255].
Here, k = 256.
'''

# set_of_numbers_to_sort = [0, 1, 2, ..., 255]
set_of_numbers_to_sort = list(range(0, 256)) 

# counted_numbers = { 0:0, 1:0, 2:0, ..., 255:0}
# this will be populated with values during sorting
# Because Python dicts use hashmaps, this implementation
# is technically expected Θ(k + n) and not guaranteed Θ(k + n)

counted_numbers = {kk : 0 for kk in set_of_numbers_to_sort}

numbers_in = input("Enter ints between 0 and 255, separated by space:\n").split(' ')

for number in numbers_in:
    counted_numbers[int(number)] += 1

for number in set_of_numbers_to_sort:
    # e.g. counted_numbers[11] = 3
    # would mean the number 11 shows up 3 times, so print it 3 times.
    
    # for each time the counted_number appeared in the original list,
    for _ in range(counted_numbers[number]):
        print(number)
        # suspicious about the nested for loop?
        # this 'smells' like O(n^2) but it isn't!
        # try this by hand with a small set if you are not convinced.







set_of_numbers_to_sort = list(range(0, 256)) 
counted_numbers = {kk : 0 for kk in set_of_numbers_to_sort}

numbers_in = input("Enter values in [0, 255] separated by space:\n")
numbers_in = numbers_in.split(' ')
for number in numbers_in:
    counted_numbers[int(number)] += 1

for number in set_of_numbers_to_sort:
    for _ in range(counted_numbers[number]):
        print(number)