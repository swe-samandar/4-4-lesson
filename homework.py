import os, random

os.system("clear")

def random_array(k, head, end):
    return [random.randint(head, end) for _ in range(k)]

def creat_array():
    array = []
    while True:
        num = int(input("Son kiriting: "))
        if not num:
            return array
        array.append(num)

""" Series14 -> K butun soni va nol soni bilan tugovchi butun sonlar ro'yxati berilgan. K sonidan kichik bo'lgan sonlar sonini chiqaruvchi programma tuzilsin. 
Agar bunday son bo'lmasa 0 chiqarilsin,"""
def func14(k):
    array = creat_array()
    print(len(list(filter(lambda n:n < k, array))))


""" Series15 -> K butun soni va nol soni bilan tugovchi butun sonlar to'plami berilgan. K sonidan katta bo'lgan birinchi son nomerini chiqaruvchi programma tuzilsin.
Agar bunday son bo'lmasa, nol chiqarilsin."""
def func15(k):
    array = creat_array()
    for i in range(len(array)):
        if array[i] > k:
            return print(i)
    return print(0) 


""" Series16 -> K butun soni va nol soni bilan tugovchi butun sonlar to'plami berilgan, K sonidan katta bo'lgan oxirgi son nomerini chiqaruvchi programma tuzilsin.
Agar bunday son bo'lmasa, nol chiqarilsin."""
def func16(k):
    array = creat_array()
    index = 0
    for i in range(len(array)):
        if array[i] > k:
            index = i
    return print(index)


""" Series17 -> B haqiqiy, n natural soni va n ta haqiqiy son berilgan. Shu sonlarni B soni bilan birga chiqaruvchi programma tuzilsin."""
def func17(b, n):
    array = random_array(n, -20, 20)
    for i in array:
        print(b, i)


""" Series18 -> n > 2 natural soni va n ta butun son o'sish tartibida berilgan. Bu sonlarni orasida bir xil qiymatlilari bo'lishi mumkin.
Har xil qiymatli elementlarni chiqaruvchi programma tuzilsin."""
def func18(n):
    array =  []
    for _ in range(n):
        array.append(int(input("Son kiriting: ")))
    
    for i in sorted(set(array)):
        print(i)


""" Series19 -> n natural soni va n ta butun son berilgan. Bu sonlar orasidan chap qo'shnisidan kichiklarini va ularning sonini chiqaruvchi programma tuzilsin."""
def func19(n):
    array = []
    for _ in range(n):
        array.append(int(input("Son kiriting: ")))

    count = 0
    for i in range(1, n):
        if array[i] < array[i - 1]:
            print(array[i])
            count += 1

    print(f"Chap qo'shnisidan kichik bo'lgan elementlar soni {count} ta.")