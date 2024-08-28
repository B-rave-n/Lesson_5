select = (input(print('Якщо бажаєш скористатися калькулятором, введи \"yes\"')))
while select == 'yes':
    number1 = int(input(print('Введи перше число:')))
    calculator_select = int(input(print('Обери дію, яку потрібно виконати:\n1. Додати\n2. Відняти\n3. Помножити\n4. Поділити')))
    number2 = int(input(print('Введи друге число:')))
    match calculator_select:
        case 1:
            print('Результат:', number1 + number2)
        case 2:
            print('Результат:', number1 - number2)
        case 3:
            print('Результат:', number1 * number2)
        case 4:
            print('Результат:', number1 / number2)
        case _:
            print('Такої дій в списку не було.')
    select = (input(print('Бажаєш знову скористатися калькулятором? Введи \"yes\"')))
print('Дію програми завершено, гарного тобі дня!')