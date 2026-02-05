"""#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [9, 5, 1, 4, 3]
insertion_sort(data)
print("Sorted using Insertion Sort:", data)

#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

numbers=[14,2,12,22,11]
print("original list: ",numbers)
sorted_list=selection_sort(numbers)
print("sorted list: ",sorted_list)
"""

def merge_sort(arr):
   
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
   
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)
    
def merge(left, right):
    result = [] 
    i = j = 0  

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

array = [2,89,45,31,4,65,35]
sorted_array = merge_sort(array)
print("Original Array =", array)
print("Sorted Array   =", sorted_array)