# from random import randint
# sp_len = int(input("Введите количество элементов списка: "))
# sp = [randint(1,20) for _ in range(sp_len)] 
# print(sp)
# min_num = int(input("Введите значение минимума: "))
# max_num = int(input("Введите значение максимума: "))



sp = [ 1, 5, 88, 100, 150, 300, 2, -4]
min_num = 33
max_num = 200


def takeClosest(sp, min_num, max_num):
    closest = sorted(sp)
    sp1 = []
    for i in closest:
        if i >= min_num and i<=max_num:
            sp1.append(i)   
    indices = [sp.index(i) for i in sp1]
    
        
            
    return indices