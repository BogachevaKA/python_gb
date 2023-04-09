a = int(input("Введите трехзначное число: "))
num1 = a%10
num2 = a//10%10
num3 = a//100
print("Результат: ", num1+num2+num3)