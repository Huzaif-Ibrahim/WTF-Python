import matplotlib.pyplot as plt

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min = 1
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

array = []
n = int(input("How many elements?? "))
for i in range(n):
    array.append(int(input(f"Enter {n+1} element :")))
    
print(f"Before swapping: {array}")
selectionSort(array)
print(f"After swapping: {array}")

x = list(range(1,10000))
plt.plot(x, [y*y for y in x])
plt.title("selection sort time complexity is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("time")
plt.show()