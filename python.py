def чи_парне_число(number):
    if (number % 2 == 0):
        return "парне"
    else:
        return "непарне"

number = input("Введіть число: ")
number = int(number)

результат = чи_парне_число(number)
print(результат)