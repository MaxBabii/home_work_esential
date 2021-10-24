#Опишите свой клас исключений. Напишите функцию, которая будет выбраивать даное исключение,
#елси пльзователь введёт опредёленное значение и перехватите это исключение при вызове функции

def main():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        print("Your name is:", name)
        print("You have:", age)
    except (ValueError, ZeroDivisionError) as error:
        print("Error", error)

if __name__ == '__main__':
    main()