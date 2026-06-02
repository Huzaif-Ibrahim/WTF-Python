import time

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[low] < pivot:
            low += 1

        while low <= high and array[high] >= pivot:
            high -= 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break    
    array[start], array[high] = array[high], array[start]
    return high


# Code for QuickSort which divides the array into two halves
def Quicksort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)

    Quicksort(array, start, p - 1)
    Quicksort(array, p + 1, end)


# Driver code to call QuickSort function
array = []

n = int(input("Enter the size of list: "))

for i in range(n):
    array.append(int(input("Enter the %d number: " % i)))

print("Before sorting: The list items are")
for i in range(len(array)):
    print(array[i], end=" ")

start = time.time()

Quicksort(array, 0, len(array) - 1)

end = time.time()

print("\nAfter sorting: The list items are", array)
print("Execution Time:", end - start)