# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    # sets base index for left and right arrays
    ind_a = 0
    ind_b = 0
    # loops through only if both arrays are greater than base index
    while ind_a < len(arrA) and ind_b < len(arrB):
        # checks if the value at the first index in the first array is less than the value of the of the first index of the second array
        if arrA[ind_a] <= arrB[ind_b]:
            # if the value of arrA is lower it gets appended to the merged array
            merged_arr.append(arrA[ind_a])
            # increments to index of arrA
            ind_a += 1
        else:
            # appends arrB ind_b to the end of merged_arr
            merged_arr.append(arrB[ind_b])
            # increments index of arrB
            ind_b += 1
    # if any elements are remaining from either array, they are added to the end of the merged list in order
    merged_arr.extend(arrA[ind_a:])
    merged_arr.extend(arrB[ind_b:])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # sets a base case for recursion, if the length of the array is 0 or 1, then the value gets returned
    if len(arr) == 0 or len(arr) == 1:
        return arr[:len(arr)]
    # sets index for half of the list
    ind_half = len(arr) // 2
    # splits the list
    left_list = arr[0:ind_half]
    right_list = arr[ind_half:len(arr)]
    # creates temporary sorted lists from each half
    temp_left = merge_sort(left_list)
    temp_right = merge_sort(right_list)
    # merge sorted lists
    arr = merge(temp_left, temp_right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

