#이중for문
#이 코드는 오류가 나는 경우가 있음
def selection_sort(list1):
    for i in range(len(list1) - 1):
        little_num = list1[i]
        for j in range((i + 1), len(list1)):
            if little_num < list1[j]:
                pass
            else:
                little_num = list1[j]

        insert1 = list1[i]
        list1[list1.index(little_num)] = insert1
        list1[i] = little_num

    return list1

list1 = [1, 4, 2, 2 , 7, 3, 10, 9, 3]
#list1 = [4, 2, 7, 1, 9, 3]
print(selection_sort(list1))

#### 2번째 풀이
list1 = [1, 4, 2, 2 , 7, 3, 10, 9, 3]
n = 0

while n < len(list1):
    min_num = list1[n+0]
    for i in range(n+1, len(list1)):
        if min_num > list1[i]:
            min_num = list1[i]
            min_index = i

    a = list1[n+0]
    if a != min_num:
        list1[n+0] = min_num
        list1[min_index] = a

    n += 1
print(list1)


## 세번째 풀이
def select_sort(list1):
    
    count = 0
    while count < len(list1)-1:
        min_num = list1[0 + count]
        min_index = 0 + count
        for i in range(1 + count, len(list1)):
            if min_num > list1[i]:
                min_index = i
                min_num = list1[i]
        a = list1[count]
        list1[count] = min_num
        list1[min_index] = a 
        
        count += 1
    return list1

list1 = [4, 2, 7, 1, 9, 3]
print(select_sort(list1))