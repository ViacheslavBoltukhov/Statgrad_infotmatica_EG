'''Найдите 5 чисел больших 500000, таких, что среди их делителей есть число,
оканчивающееся на 8, при этом этот делитель не равен 8 и самому числу. В
качестве ответа приведите 5 наименьших чисел, соответствующих условию.
Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке
сначала выводится само число, затем минимальный делитель, оканчивающийся на
8, не равный 8 и самому числу'''
start=500000
k=0
while k!=5:
    start+=1
    for i in range(18,start,10):
        if start%i==0:
            k+=1
            print(start,i)
            break
