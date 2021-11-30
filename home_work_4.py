lst = [1, 2, 3, 4, 5]
it = iter(lst)
lst.reverse()

for i in range(5):
    print(next(it))


