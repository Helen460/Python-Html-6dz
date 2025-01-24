#1. Створити список з 5 чисел, а потім вивести його у зворотному порядку.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

#2. Створити список із 20 випадкових чисел. Вивести всі елементи масиву з парними індексами.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Парні числа від 1 до 20:", even_numbers)

#3. Написати програму, яка пропонує користувачу ввести число і потім підраховує, скільки разів це число зустрічається у списку зі 100 випадкових елементів.
import random
random_list = [random.randint(0, 100) for _ in range(100)]
number = int(input("Введіть число для пошуку: "))
count = random_list.count(number)
print("Число зустрічається:", count, "раз(и) у списку з випадкових чисел.")

#7. Створити список рядків на 3999 елементів. Заповнити його римськими числами від 1 до 3999, показати на екрані всі елементи.
roman_numerals = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I")
]
roman_list = []
for num in range(1, 4000):
    roman = ''
    n = num
    for value, numeral in roman_numerals:
        while n >= value:
            roman += numeral
            n -= value
    roman_list.append(roman)
for roman in roman_list:
    print(roman)

#8. Ввести число в діапазоні від 0 до 1000000. Озвучити його словами. Наприклад, при введенні числа 25 вивести на екран «двадцять п’ять».
import random
ones = ["", "один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев’ятнадцять"]
tens = ["", "", "двадцять", "тридцять", "сорок", "п’ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев’яносто"]
hundreds = ["", "сто", "двісті", "триста", "чотириста", "п’ятсот", "шістсот", "сімсот", "вісімсот", "дев’ятсот"]
thousands = ["", "тисяча", "дві тисячі", "три тисячі", "чотири тисячі", "п’ять тисяч", "шість тисяч", "сім тисяч", "вісім тисяч", "дев’ять тисяч"]
n = int(input("Введіть число від 0 до 1000000: "))
words = []
if n >= 1000:
    thousands_part = n // 1000
    words.append(thousands[thousands_part])
    n %= 1000
if n >= 100:
    hundreds_part = n // 100
    words.append(hundreds[hundreds_part])
    n %= 100
if n >= 20:
    tens_part = n // 10
    ones_part = n % 10
    words.append(tens[tens_part])
    if ones_part > 0:
        words.append(ones[ones_part])
elif n >= 10:
    words.append(teens[n - 10])
elif n > 0:
    words.append(ones[n])
if n == 0 and len(words) == 0:
    print("нуль")
else:
    for word in words:
        print(word, end=' ')

#9. Створити список списків розміром M х N, заповнений випадковими числами з діапазону від -10 до 10. Визначити кількість додатних, від’ємних і нульових елементів.
import random
M = 5
N = 5
matrix = []
for y in range(M):
    row = []
    for x in range(N):
        row.append(random.randint(-10, 10))
    matrix.append(row)
for y in range(M):
    for x in range(N):
        print(matrix[y][x], end='  ')
    print()
positive_count = 0
negative_count = 0
zero_count = 0
for y in range(M):
    for x in range(N):
        if matrix[y][x] > 0:
            positive_count += 1
        elif matrix[y][x] < 0:
            negative_count += 1
        else:
            zero_count += 1
print("Кількість додатних елементів:", positive_count)
print("Кількість від'ємних елементів:", negative_count)
print("Кількість нульових елементів:", zero_count)

#10. Створити список списків розміром M х N, заповнений випадковими числами з діапазону від 0 до 20. Визначити суму для кожного рядка і для кожного стовпця.
import random
matrix = []
M = 5
N = 5
for y in range(M): 
    row = []
    for x in range(N):
        row.append(random.randint(0, 20)) 
    matrix.append(row)
for y in range(M):
    for x in range(N):
        print(matrix[y][x], end='  ')
    print()
row_sums = []
for y in range(M):
    row_sum = 0
    for x in range(N):
        row_sum += matrix[y][x]
    row_sums.append(row_sum)
print("Сума для кожного рядка:")
for i, row_sum in enumerate(row_sums):
    print(row_sum)
col_sums = []
for x in range(N):
    col_sum = 0
    for y in range(M):
        col_sum += matrix[y][x]
    col_sums.append(col_sum)
print("Сума для кожного стовпця:")
for i, col_sum in enumerate(col_sums):
    print(col_sum)

#11. Заповнити квадратну матрицю розміром M х N по спіралі. Число 1 ставиться у центр матриці, а потім масив заповнюється по спіралі проти годинникової стрілки значеннями за зростанням.
import random
M = 5
N = 5
matrix = [[0] * N for _ in range(M)]
x, y = M // 2, N // 2
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction_idx = 0
steps = 1
matrix[x][y] = 1
current_value = 2
while current_value <= M * N:
    for _ in range(steps):
        x += directions[direction_idx][0]
        y += directions[direction_idx][1]
        if 0 <= x < M and 0 <= y < N:
            matrix[x][y] = current_value
            current_value += 1
    direction_idx = (direction_idx + 1) % 4
    if direction_idx % 2 == 0:
        steps += 1
print("Матриця:")
for row in matrix:
    print(" ".join(f"{num:3}" for num in row))