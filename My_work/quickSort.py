 # sort algoritham
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot=arr[len(arr) // 2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x== pivot]
    right=[x for x in arr if x >pivot]
    return quickSort(left)+middle +quickSort(right)


arr=[3,4,5,6,8,10,2,1,1,2,3,5,2]
print(quickSort(arr))

# searching
def first_occurence(arr,target):
    left,right =0,len(arr) - 1
    result=-1

    while left <= right:
          mid=left + (right - left ) // 2

          if arr[mid] == target:
               result = mid
               right  =mid -1
          elif arr[mid] <target:
               left=mid +1
          else:
               right=mid -1
    return result

print(first_occurence(arr,3))

#selection sort
A = [11, 23, 10, 9, 14, 12, 23, 20, 34, 27]

def selection_sort(A):
    for i in range(len(A)-1):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

print(selection_sort(A))

#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    left_idx, right_idx = 0, 0
    
    # Merge the two sorted lists
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1
    
    # If there are remaining elements in left or right, add them
    sorted_list.extend(left[left_idx:])
    sorted_list.extend(right[right_idx:])
    
    return sorted_list

arr = [11, 23, 10, 9, 14, 12, 23, 20, 34, 27]
sorted_arr = merge_sort(arr)
print(sorted_arr)

