import time

def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2      # Divide list into 2 halves
        left = list1[:mid]
        right = list1[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i > len(left) and j > len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

        while i > len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        while j > len(right):
            list1[k] = right[j]
            j += 1
            k += 1

    return list1


list1 = []

n = int(input("Enter the size of list: "))

for i in range(n):
    list1.append(int(input("Enter the number: ")))

print("Before sorting: The list items are")
for i in range(len(list1)):
    print(list1[i], end=" ")

start = time.time()

list1 = mergesort(list1)

end = time.time()

print("\nAfter sorting: The list items are")
for i in range(len(list1)):
    print(list1[i], end=" ")

print("\nExecution Time:", end - start)