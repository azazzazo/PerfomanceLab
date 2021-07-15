decimal = int(input("Введите десятичное число: \n"))
convert = int(input("Конвертировать в: [1] Двоичную, [2] Троичную, [3] Шестнадцетиричную: \n"))

if convert == 1:
    print("Конертация в двоичную \n", bin(decimal))
elif convert == 2:
    print("Конвертация в восьмеричную \n", oct(decimal))
elif convert == 3:
    print("Конвертация в шестнадцетиричную \n", hex(decimal))
else:
    print("Введите десятичное число")
