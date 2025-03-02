a = int(input())
if (
        ((0 < a <= 10 or 19 <= a <= 28) and a % 2 == 0)
        or (11 <= a <= 18 or 29 <= a <= 36)
        and a % 2 != 0):
        print("черный")
elif a == 0:
    print("зеленый")
elif 0 > a or a > 36:
    print("ошибка ввода")
else:
    print("красный")

