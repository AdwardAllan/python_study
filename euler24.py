import itertools

# print([x for x in itertools.islice(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10),999999,1000000)])
print([x for x in itertools.islice(itertools.permutations([0,1,2],3),5,6)])
