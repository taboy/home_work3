#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list=[1.1, 1.2, 3.1, 5, 10.01]

list1=[]
for y in (list):
    x=((y-int(y)))
    x=round(x,2)
    if x!=0:
        list1.append(x)    
print(list1)
for y in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp

print(list1[len(list1)-1]-list1[0])
