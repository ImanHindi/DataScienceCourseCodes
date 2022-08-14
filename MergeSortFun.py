#Merge Sort Fun.
def merge(left, right):
    
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

def Merge_Sort_fun(l):
    if len(l)>1:
        ind =int(len(l)/2)
        left= Merge_Sort_fun(l[:ind])
        right=Merge_Sort_fun(l[ind:])
    elif len(l)==1:
        return l
    return merge(left,right)


l=[5,3,2,7,9,8,1,10]
print(l)
print(Merge_Sort_fun(l))



def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list

    mid_point = list_length // 2

    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    return merge(left_partition, right_partition)



def run_merge_sort():
    unsorted_list = [2, 4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    #print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    #print(sorted_list)


run_merge_sort()


