# import matplotlib.pyplot as plt

# def bubbleSort(array):
#     n = len(array)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#         print(array)
#     return array

# array = []
# n = int(input('How many elements do you want in the array : '))
# for i in range(n):
#     array.append(int(input(f"Enter {i+1} element : ")))
# print(f'Array before swapping : {array}')
# array = bubbleSort(array)
# print(f"Array after sorting: {array}")

# x=list(range(0, 10000))
# y = list([y*y for y in x])

# plt.plot(x, y)
# plt.title("Bubble sort - Time Complexity is O(n\u00b2)")
# plt.xlabel("Input")
# plt.ylabel("Time")
# plt.show()


import matplotlib.pyplot as plt

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
n = int(input("Enter the elements you want in array: "))
for i in range(n):
    a.append(int(input(f"Enter {i} element: ")))
    
print(f"Array before swapping: {a}")
bubbleSort(a)
print(f'Array after swapping {a}')

x = list(range(1,10000))
plt.plot(x, [y*y for y in x])
plt.title("Time complexity of bubble sort is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()