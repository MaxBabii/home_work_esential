# Напишите программу, которая вводит с клавиатуры последовательность чисел
# и выводит её отсортированой в порядке возрастания

a = input("Enter numbers: ").split()

def function(a):
    a.sort()
    print(a)

function(a)


