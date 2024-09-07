import string
import keyword
strings = [i for i in string.punctuation if i != '_']
strings.extend([' ', '__'])

zminna = input('Яку назву змінної ми перевіримо?')
while 1:
    count_of_strings = 0
    for i in strings:
        if i in zminna:
            count_of_strings = 1
    if zminna in keyword.kwlist or count_of_strings:
        zminna = input('Не можна використовувати спецслова та спецсимволи. Введи іншу назву змінної:')
        continue
    elif zminna[0].isdigit() or not zminna.lower != zminna:
        zminna = input('Змінна не може починатися з цифри та містити великі літери. Введи іншу назву змінної:')
        continue
    else:
        print("Можеш так назвати свою змінну")
        break