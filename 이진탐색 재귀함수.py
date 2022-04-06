def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스

    if end_index == None:
        end_index = len(some_list) - 1
        
        
    if len(some_list) == 0: 
        return None
    elif len(some_list) == 1:
        if element == some_list[0]:
            return 0       
        return None
    
    if start_index > end_index:
        return None
    
    average_index = (start_index + end_index) // 2
    if some_list[average_index] == element:
        return average_index
    elif some_list[average_index] < element:
        return binary_search(element, some_list, start_index=average_index+1, end_index=len(some_list))
    else:
        return binary_search(element, some_list, start_index=0, end_index=average_index-1)
    
    # 코드를 작성하세요.

print(binary_search(2, []))
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


#### 두번째 풀이
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    mid_index = (start_index + end_index) // 2

    if start_index > end_index:
        return None

    if element == some_list[mid_index]:
        return mid_index
    elif element > some_list[mid_index]:
        start_index = mid_index + 1
        return binary_search(element, some_list, start_index, end_index)
    elif element < some_list[mid_index]:
        end_index = mid_index-1
        return binary_search(element, some_list, start_index, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

###세번째 풀이
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    if start_index > end_index:
        return None

    mid = (start_index + end_index) // 2
    if some_list[mid] == element:
        return mid
    elif some_list[mid] < element:
        start_index = mid + 1
    elif some_list[mid] > element:
        end_index = mid - 1

    return binary_search(element, some_list, start_index, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


#### 이거는 재귀없이 푸는 코드잇 정답
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

###이거는 재귀없이 내풀이
def binary_search(element, some_list):
    # 코드를 작성하세요.
    f_index = 0
    e_index = len(some_list) - 1


    for i in range((len(some_list) // 2) + 1) :
        mid = (f_index + e_index) // 2
        if element == some_list[mid]:
            return mid
        elif element > some_list[mid]:
            f_index = mid + 1
        elif element < some_list[mid]:
            e_index = mid - 1
    return None


print(binary_search(40, [2, 3, 5, 7, 11, 13, 15, 17 ,20, 32, 40, 58]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
