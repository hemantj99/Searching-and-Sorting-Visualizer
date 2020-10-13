def bubbleSort(arr):
    length = len(arr) #finding the length of array to be sorted

    for i in range(length): # executing the outer loop
        for j in range(0,length-i-1): # execiting the inner loop
            if arr[j]>arr[j+1]: # comparing two consecutive values
                arr[j], arr[j+1] = arr[j+1], arr[j] #swapping the values if latter is greater
    return arr


def bubbleSortOptimized(arr):
    length = len(arr) #finding the length of array to be sorted
    for i in range(length): # executing the outer loop
        for j in range(0,length-i-1): # execiting the inner loop
            swapped = False #checking if any swaps take place in the ith interation
            if arr[j]>arr[j+1]: # comparing two consecutive values
                arr[j], arr[j+1] = arr[j+1], arr[j] #swapping the values if latter is greater
                swapped = True
        if swapped==False:
            break #break off the outer loop if there are no swaps in an iteration
    return arr

arr = [3,5,2,4,0,1]
sorted_arr = bubbleSort(arr)
print(sorted_arr)

arr = [3,5,2,4,0,1]
sorted_arr = bubbleSortOptimized(arr)
print(sorted_arr)