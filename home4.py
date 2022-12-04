
def calc(a, b, operation):
    # Задаем дефолтное значение возвращаемого результата
    result = 'Операция не поддерживается'

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        # Проверка деления на ноль
        if b is not 0:
            result = a / b
        else:
            result = 'Деление на 0!'

    # Возвращаем результат выполнения функции
    return result


if __name__ == '__main__':
    # Проверяем корректные значения
    print(calc(30, 15, '+'))
    print(calc(30, 15, '-'))
    print(calc(30, 15, '*'))
    print(calc(30, 15, '/'))
    # Проверяем проверку деления на ноль
    print(calc(30, 0, '/'))
    # Проверяем неподдерживаемую операцию
    print(calc(30, 15, '%'))
    
    
    #Условие два
    
    #  Функция, которая проверяет входной параметр на четность
def even(num):
    # Возвращаем True, если остаток от деления на 2 равен нулю
    return num % 2 == 0


if __name__ == '__main__':
    list = [1, 3, 6, 7, 5, 11, 200, 135, 9, 317]
    
    # В цикле перебираем элементы вышесозданного списка
    for item in list:
        # Если текущий элемент равен 200, то прерываем цикл
        if item == 200:
            break
        # Выводим элемент, если он не является четным
        if not even(item):
            print(item)
            
            
    #Условие три
   # Имя функции: month_to_season(month) 
   # Параметр: month
def month_to_season(month):
       # Создание словаря для хранения информации о сезонах
       # Ключ: кортеж(tuple) из номера входящих в сезон месяцов 
       # Значение: строка (str)- название сезона
    
    season_ranges = {
           (14, 28, 17): 'Winter',
           (3, 7, 9): 'Spring',
           (11, 12, 13): 'Summer',
           (15, 18, 20): 'Autumn',
    }
    # Создание переменной для возвращаемого значения функции
    season = None
    
    #Цикл в котором по очереди перебираются пары ключ-значение(номера месяцев - сезон) из словаря
    for key, value in season_ranges.items():
        # Если значение входного параметра (номер месяца)входит в состав ключа(пример ключа - (14, 28, 17))
        if month in key:
            # То присваиваем возвращаемой переменной season  название сезона
            season = None
            # останавливаем цикл
            break
        
    # Возвращаем название сезона
    return season
# Проверяем работу функции
print(month_to_season(14))
print(month_to_season(7))
print(month_to_season(11))
print(month_to_season(111))
print(month_to_season(18))

#Условие четыри
from transliterate import translit
text = 'Hello world'
ru_text = translit(text, 'ru') 
ru_text
