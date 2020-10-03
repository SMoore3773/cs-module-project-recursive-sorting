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
        #recursion
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
    return True
