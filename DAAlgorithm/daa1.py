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
"""
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
""""""
def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from left and right halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))