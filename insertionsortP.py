def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        item = array[i]
        j = i-1
        while j >= 0 and item < array[j]:
            array[j+1] = array[j]
            j = j-1
            array[j+1] = item 
    return array

def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k+=1
            
        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1
            
        while j < len(right):
            list[k] = right[j]
            j+=1
            k+=1
            
    return list
        
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr    
        
def quickSort(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    
    while True:
        while low <= high and arr[low] < pivot:
            low+=1
        while low <= high and arr[high] >= pivot:
            high-=1
        
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
        
    arr[start], arr[end] = arr[end], arr[start]
    return high