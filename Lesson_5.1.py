import string
import keyword
strings = []
for i in string.punctuation:
    strings += i
strings.remove('_')
strings.extend([' ', '__'])
zminna = input(print('Яку назву змінної ми перевіримо?'))
while zminna == zminna:
    spec_words = 0
    spec_strings = 0
    count_capital = 0
    result = bool
    for i in keyword.kwlist:
        if zminna == i:
            spec_words += 1
    for i in strings:
        count = zminna.count(i)
        if count != 0:
            spec_strings += 1
    for i in zminna:
        if i.isupper() == True:
            count_capital += 1
    if spec_strings > 0:
        result = False
        zminna = input(print(result, 'Не можна використовувати спецсимволи, пробіл та "__". Введи іншу назву змінної:'))
        continue
    else:
        if spec_words > 0:
            result = False
            zminna = input(print(result, 'Не можна використовувати спецслова. Введи іншу назву змінної:'))
            continue
        else:
            if zminna[0].isnumeric():
                result = False
                zminna = input(print(result, 'Змінна не може починатися з цифри. Введи іншу назву змінної:'))
                first_symbol = 0
                continue
            else:
                if count_capital > 0:
                    result = False
                    zminna = input(print(result, 'Змінна не може не може містити великі літери. Введи іншу назву змінної:'))
                    continue
                else:
                    result = True
                    print(result, 'Можеш так назвати свою змінну')
                    break