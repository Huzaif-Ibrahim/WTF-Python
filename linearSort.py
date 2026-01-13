import time 
import matplotlib.pyplot as plt

def linearSearch(a, key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1

start = time.time()
a = [3,5,11,56,6,22,90]
print(f'The array elements are {a}')
key = int(input('Input a value to search in array : '))
result = linearSearch(a, key)

if(result == -1):
    print(f'Sorry no element found.')
else:
    print(f'Element found at index {result + 1}')

end = time.time()
print(f'Program runtime { end - start }')

x = list(range(1, 10000))
plt.plot(x, [y for y in x])
plt.title('Linear search time complexity is Big O(n)')
plt.xlabel('Input')
plt.ylabel('Time')
plt.show()