# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # print('target: ', target)
    # print('arr[middle]: ', arr[middle])
    # print('middle', middle)
    if end >= start:
        # sets middle index
        middle = (start + end) // 2
        # base case for recursion, if middle value is target, return
        if arr[middle] == target:
            return middle
        # recursion
        elif arr[middle] > target:
            # moves middle to the left of the BST and re-runs search
            return binary_search(arr, target, start, middle - 1)
        elif arr[middle] < target:
            # moves middle to the right of the BST and re-runs search
            return binary_search(arr, target, middle + 1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    first = 0
    last = (len(arr) - 1)
    found = False
    # check for ascending order
    if arr[first] <= arr[last]:
        while first <= last and not found:
            middle = (first + last) // 2
            if arr[middle] == target:
                found = middle
            else:
                if target < arr[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
        if found is False:
            return -1
    # check for descending order
    if arr[first] > arr[last]:
        # while the first item in the array is still larger and the target is not found
        while arr[first] >= arr[last] and not found:
            # change the middle value to the middle value of the array
            middle = (first + last) // 2
            # check middle for target value, if found return arrau index
            if arr[middle] == target:
                found = middle
            else:
            # if the target is smaller than the number at the middle index
                if target < arr[middle]:
                    # shift the starting index to the index to the right of the current middle
                    first = middle + 1
                else:
                    # otherwise, the target is larger, and the new ending index will be the index to the left of the current middle
                    last = middle - 1
        # if the program falls out of the while loop and the target is still flase
        if found is False:
            # return falsy value
            return -1
    # return index of target value
    return found
