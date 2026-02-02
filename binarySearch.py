# import time

# def binarySearch(a , low, high, key):
#     if low > high or key not in a:
#         print("Unseccessful operation")
#         return
#     mid = (high+low)//2
#     if(a[mid] == key):
#         print(f'The key is at index {mid}')
#         return 
#     elif(key > a[mid]):
#         binarySearch(a, mid+1, high,key)
#     else:
#         binarySearch(a, low, mid-1,key)
        
# a = []
# n = int(input("How many elements do you want in a array : "))

# for i in range(n):
#     a.append(int(input(f"Enter the {i+1} element : ")))
    
# key = int(input("Enter the key: "))
# start = time.time()
# binarySearch(a, 0, len(a) - 1, key)
# end = time.time()

# print(f'Time took for the operation : {end-start}')

import time

def binarySearch(a, low, high, key):
    if low > high:
        print('Unseccessful Operation')
        return
    
    mid = (high+low) // 2
    if key == a[mid]:
        print(f'The element {key} is at index {mid}')
        return
    elif(key > a[mid]):
        binarySearch(a, mid+1, high, key)
    else:
        binarySearch(a, low, mid-1, key)
        
a = []
n = int(input('Enter the elements you want in array: '))

for i in range(n):
    a.append(int(input(f'Enter the {i+1} element: ')))
    
key = int(input('Enter the element to search: '))

start = time.time()
binarySearch(a, 0, len(a)-1, key)
end = time.time()

print(f'The time taken for binary search is: {end-start}')
