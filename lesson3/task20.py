list_scrabble = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

word = input("Введите слово: ").upper()
summ = 0
for i in word:
    for a, b in list_scrabble():
        if i in b:
            summ += a
print(f"Стоимость слова: {summ}")