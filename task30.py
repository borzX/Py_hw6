start = int(input("Введите первый элемент прогрессии: "))
step = int(input("Введите шаг прогрессии: "))
len = int(input("Введите длину прогрессии: "))

def progresia(start, step, len):
    temp_list = []
    num = start
    for i in range(len):
        temp_list.append(num)
        num=step+num      
    return temp_list
        
print(progresia(start, step, len))