def insert_sort(list1):
    for i in range(1, len(list1)):
        for j in range(i-1, -1, -1):
            if list1[i] < list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
                i -= 1
    return list1



print(insert_sort(list1 = [4, 2, 7, 1, 9, 3,11,21,19,30,47,38]))


#### 두번째 풀이
list1 = [4, 2, 1 ,7, 1, 9, 30, 3,  3, 10]


for i in range(1, len(list1)):
    b = i-1
    for j in list1[i-1::-1]:
        if j > list1[i]:
            a = j    
            list1[b] = list1[i]
            list1[i] = a
            b -= 1
            i -= 1

print(list1)


### 3번째 풀이
def insert_sort(list1):

    count = 0
    while count < len(list1)-1:
        num = list1[1 + count]

        for i in range(count, -1, -1):
            if list1[i] > num:
                #a = list1[i] 
                list1[i], list1[i+1] = num, list1[i]
                #list1[i+1] = a

        count += 1 
    
    return list1

#list1 = [2, 4, 7, 1, 9, 3]
list1 = [4, 2, 7, 1, 9, 3]
print(insert_sort(list1))