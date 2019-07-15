def selection_sort( arr ):
    # loop through n-1 elements
    max_idx = len(arr)
    for current_idx in range(max_idx - 1):
        current_val = arr[current_idx]
        min_val_idx = current_idx

        # find next smallest element
        for idx in range(current_idx, max_idx):
            if arr[idx] < arr[min_val_idx]:
                 min_val_idx = idx

        # swap
        arr[current_idx] = arr[min_val_idx]
        arr[min_val_idx] = current_val

    return arr


def bubble_sort(arr):
    swap_made = False
    for idx in range(len(arr) - 1):
        curr_val = arr[idx]
        next_val = arr[idx+1]
        if next_val < curr_val:
            arr[idx] = next_val
            arr[idx+1] = curr_val
            swap_made = True

    if swap_made:
        return bubble_sort(arr)
    else:
        return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr