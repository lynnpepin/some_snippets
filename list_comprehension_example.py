doubles = [2*x for x in range(4)]
print(doubles)

sixes = [2*y for y in [3*x for x in range(4)]]
print(sixes)

nested_list = [[1,2], [10,20], [100,200]]
alt_sixes = [x*y for x, y in nested_list]
print(alt_sixes)
