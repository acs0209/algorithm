##첫번째 풀이
def merge(list1, list2):
    # 코드를 작성하세요.
    new_list = []

    if list1 == []:
        new_list = list2
        return new_list
    if list2 == []:
        new_list = list1
        return new_list

    if list1[-1] < list2[0]:
        for i in list1:
            new_list.append(i)
        for j in list2:
            new_list.append(j)
        return new_list

    if list1[0] > list2[-1]:
        for i in list2:
            new_list.append(i)
        for j in list1:
            new_list.append(j)
        return new_list

    for i in list1:
        for j in list2:
            if i < j and i not in new_list:
                new_list.append(i)
                break           
            elif i > j and j not in new_list:
                new_list.append(j)
    if list1[-1] < list2[-1]:
        new_list.append(list2[-1])

    return new_list



### 두번째 풀이
def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    if list1 == []:
        return list2
    if list2 == []:
        return list1
    
    a = 0
    b = 0
    new_list = []
    while True:
        if list1[a] >= list2[b]:
            new_list.append(list2[b])
            b += 1
        elif list1[a] <= list2[b]:
            new_list.append(list1[a])
            a += 1

        if b == len(list2):
            new_list = new_list + list1[a:]
            break
        if a == len(list1):
            new_list = new_list + list2[b:]
            break
    
    return new_list

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))