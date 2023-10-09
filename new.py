l1 = [1,2,3,4,5]
result = filter(lambda x : x % 2 == 0,l1)
print(list(result))

l2 = [1,2,3,4,5,6]
result = map(lambda x : x+x , l2)
print(list(result))
