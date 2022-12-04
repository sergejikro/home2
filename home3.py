def x_dict(list1, list2):
    a = {}
    for x, y in zip(list1, list2):
        a.update(dict([(x, y)]))
    return a


print(x_dict(['Elliot', 'Spencer', 'John'], ['01/01/2000', '09/10/1999', '21/12/1990']))

#задача №2 from collections import OrderedDict
dct = "Ordered_Dict"({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})

# Меняем местами первый и последний элементы

first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)

# Удаляем второй элемент

second = list(dct.items())[1]
del dct[second[0]]

# Вставляем новый элемент
dct['new_key'] = 'new_value'
"my_dict"
{5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'}
id("my_dict")
17128656
"start_dict_id"
17128656
 

#задача три

my_list = [2, 4, 8]
print(my_list[::-1])

#четвертое задание

if __name__ == '__main__':
 
    l = ['A', 'B', '', 'C', '', 'D']
    l = [s for s in l if s]
    print(l)    # ['A', 'B', 'C', 'D']
    
    
    #задача 5
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if 'j' in b:
        if i == 'j':
            c.append(i)
            break
print(c)
print(i)
i += 1
        