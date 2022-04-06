# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가 시킨다
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다
    swap_elements(my_list, b, p)
    p = b

    # pivot의 최종 인덱스를 리턴해 준다
    return p

def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    #base case
    if end - start < 1:
        return 
    
    pivot_index = partition(my_list, start, end)
    quicksort(my_list, start, pivot_index-1)
    quicksort(my_list, pivot_index+1, end)
    #return quicksort(my_list, start1, end1)#, quicksort(my_list, start2, end2)

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
#list1 = [1, 3, 5, 7, 9, 11, 13, 11]
print(quicksort(list1, 0, len(list1) - 1))
print(list1)
# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)



####두번째 풀이
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    #return my_list
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = end 
    i_index = start
    b_index = start

    for i in range(start, pivot):
        if my_list[pivot] < my_list[i]:
            i_index += 1
        else:
            swap_elements(my_list, i_index, b_index)            
            i_index += 1
            b_index += 1
    swap_elements(my_list, b_index, len(my_list)-1)
    
    return b_index

# 퀵 정렬
def quicksort(my_list, start, end):
    # base case
    if end - start < 1:
        return

    a = partition(my_list, start, end)

    quicksort(my_list, start, a - 1)
    quicksort(my_list, a + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)



###내 방법(고쳐야 할 부분 있음)
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    p = my_list[end]
    #big_index = start
    #i_index = start
    s_index = start

    for k in range(end+1):
        if k == end:
            my_list[s_index], my_list[k] = my_list[k], my_list[s_index]
            #break        
        #if my_list[k] > p:
            #i_index += 1
            #big_index += 1
            #pass
        if my_list[k] < p:
            #i_index += 1
            swap_elements(my_list, s_index, k)
            s_index += 1
        
    return s_index
# 테스트 1
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    
    #base case
    if end - start < 1:
        return 
    else:
        pivot_index = partition(my_list, start, end)
        quicksort(my_list, start, pivot_index-1)
        quicksort(my_list, pivot_index+1, end)
    #return quicksort(my_list, start1, end1)#, quicksort(my_list, start2, end2)

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
#list1 = [1, 3, 5, 7, 9, 11, 13, 11]
print(quicksort(list1, 0, len(list1) - 1))
print(list1)
# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)