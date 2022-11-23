'''no name sort'''
a=[6,3,2,5,1,81,3,71,15,65,5,34,8,9,21,45,1,4,5,6,8,9,12,15,42]
count=0
for i in range(len(a)):
    for j in range(i,len(a)):
        count+=1
        if a[j]<a[i]:
            a[j],a[i]=a[i],a[j]
print(a)
print(count)


'''сортировка вставкой #1'''
data=[6,3,2,5,1,81,3,71,15,65,5,34,8,9,21,45,1,4,5,6,8,9,12,15,42]
for i in range(1,int(len(data))):
    for j in range(i-1,-1,-1):
        temp =data[j+1]
        if temp<data[j]:
            data[i]=data[j]
            data[j]=temp
            i-=1
print(data)


'''сортировка вставкой #2'''
data1 = [6,3,2,5,1,81,3,71,15,65,5,34,8,9,21,45,1,4,5,6,8,9,12,15,42]
for i in range(int(len(data1))):
    key=data1[i]
    while key<data1[i-1]and i>=1:
        data1[i]=data1[i-1]
        i-=1
        data1[i]=key
<<<<<<< HEAD
print(f'Отсортированый список: {data1}')
=======
print('Вот получившийся список :',data1)
>>>>>>> second

new_sort = [1,2,3,4,5,6,7,8]