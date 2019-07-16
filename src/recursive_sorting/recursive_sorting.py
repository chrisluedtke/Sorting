# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr_a, arr_b):
    merged_arr = []
    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] <= arr_b[0]:
            merged_arr.append(arr_a.pop(0))
        else:
            merged_arr.append(arr_b.pop(0))
    
    return merged_arr + arr_a + arr_b


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if type(arr[0]) != list:
        arr = [[i] for i in arr]  # make each element a list
    for idx in range(len(arr) // 2):
        arr[idx:idx+2] = [merge(arr[idx], arr[idx+1])]
    if len(arr) > 1:
        return merge_sort(arr)
    else:
        return arr[0]


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
