#Условие первое 
def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

# Тесты
print(sum_range(8, 16))
print(sum_range(-2, 2))
print(sum_range(5, 4))

#Условие второе и третье

print('%02d:%02d' %('h, m'))

print('{:02}:{:02}'.format('h, m'))

h1, h2 = int(input()), int(input())
m1, m2 = int(input()), int(input())
Hour = (h1 + h2(m1 + m2) / 60) //24
Mins = (m1 + m2) /60
print(str('hour') + ':' + str('mins'))

#Условие четвертое

a1 = int(input())
print('YES') if ((a1 % 4 == 0) and not (a1 % 100 == 0)) or (a1 % 400 == 0) else print('NO')
