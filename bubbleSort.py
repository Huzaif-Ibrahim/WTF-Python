# import matplotlib.pyplot as plt

# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         swapped = False
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if swapped == False:
#             break
#     return arr

# a = []
# n = int(input("Enter the elements you want in array: "))
# for i in range(n):
#     a.append(int(input(f"Enter {i} element: ")))
    
# print(f"Array before swapping: {a}")
# bubbleSort(a)
# print(f'Array after swapping {a}')

# x = list(range(1,10000))
# plt.plot(x, [y*y for y in x])
# plt.title("Time complexity of bubble sort is O(n\u00b2)")
# plt.xlabel("Input")
# plt.ylabel("Time")
# plt.show()

import matplotlib.pyplot as plt
import time

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

a = []
n = int(input('Enter the elements you want in array: '))
for i in range(n):
    a.append(int(input(f'Enter {i+1} element: ')))
    
print(f'Your array is: {a}')
start = time.time()
a = bubbleSort(a)
end = time.time()
print(f'Sorted array: {a}')
print(f'Runtime is {end-start}')

x = list(range(1,10000))
plt.plot(x, [y*y for y in x])
plt.title("Bubble sort time complexity is O(n\u00b2)")
plt.xlabel("Time")
plt.ylabel("Input")
plt.show()