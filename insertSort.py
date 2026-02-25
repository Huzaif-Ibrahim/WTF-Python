import matplotlib.pyplot as plt 

def insertionsort(array): 
    n=len(array) 
    for i in range(1,n): 
        item=array[i] 
        j=i-1 
        while j>=0 and item<array[j]: 
            array[j+1]=array[j] 
            j=j-1 
            array[j+1]=item 
    return array 
 
array=[] 
n=int(input("How many elements??")) 
for i in range(n): 
    array.append(int(input("Enter %d number:" %i))) 
print(f"before swapping:{array}") 
array=insertionsort(array) 
print(f'After swapping:{array}') 
x=list(range(1,10000)) 
plt.plot(x , [y*y for y in x] ) 
plt.title("Insertion Sort- Time Complexity is O(n\u00b2)") 
plt.xlabel("Input") 
plt.ylabel("Time") 
plt.show()

# insertion sort --> only plot
# bubble sort --> only plot
# linear search --> time and plot
# binary search --> only time
# stack adt