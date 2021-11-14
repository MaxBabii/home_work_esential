# Example

# a = [1, 2, 3]
# it = iter(a)
# next(it)


# Example1

# lst = (x for x in range(1000000000))
# for i in lst:
#     print(i, end=" ")
#     if i > 100:
#         break
# print("new loop")
#
# for i in lst:
#     print(i, end=" ")
#     if i > 200:
#         break
# Operatory

# b = (x ** 2 for x in range(10))
#
# # print(sum(b))
#
# # 2
#
# a = list(b)
# print(a)

# Example2

# 1

# def getAllAverage(N):
#     avs = []
#     count = 0
#     S = 0
#     for i in range(1, N + 1):
#         count += 1
#         S += i
#         avs.append(S/count)
#
#     return avs
#
# print(getAllAverage(100))

# 2

# def getAllAverage(N):
#     avs = []
#     count = 0
#     S = 0
#     for i in range(1, N + 1):
#         count += 1
#         S += i
#         # avs.append(S/count)
#         yield S/count
#
# it = getAllAverage(10)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# Example 3

# def f():
#     for x in range(10):
#         yield x
#
# s = f()
# print(s)
#
# print(next(s))
# print(next(s))
# print(next(s))


# Ітератори і генератори використовуються для того щоб економити памʼять компʼютера
# (заміна створення листів)