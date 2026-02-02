import time
import matplotlib.pyplot as plt

def linearSearch(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

arr = [5,7,2,4,1,9,8,0]
start = time.time()
print("The elements are: ",arr)
key = int(input("Enter the key: "))
index = linearSearch(arr, key)
end = time.time()
if(index == -1):
    print("Unsuccessfull!")
else:
    print(f"The key is at index: {index}")

print("Runtime of Linear Search is: ",end-start)

x = list(range(1,10000))
y = list([y for y in x])
plt.plot(x, y)
plt.title("Time complexity of linear search is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()