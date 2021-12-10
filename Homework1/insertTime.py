###############################
## FIle name: insertTime.py
## Name: JIanglong Yu
## Date: 6/27
## descripution: This code will recording the time of insert sort to sort list with differet size.
#################################
import time
import random as r

# insert sort
def insertsort(arr):
    for i in range(1, len(arr)):
        # temp is insertion element
        temp = arr[i]
        j = i
        # when the j is greater than 0 and the insertion element is less than the left element, 
        # they will swap the position constantly.
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
    return arr

# Print running time and arr size
def result_fun(n):
    # Generates n numbers with a range of 0-10000 and put them into an arr 
    arr = r.choices(range(0,10000), k=n)
    # Start collecting time
    start = time.perf_counter()
    insertsort(arr)
    # End time
    end = time.perf_counter()
    # Convert the time unit from second to milisecond 
    f = (end-start) * 1000
    # Prin the array size and running time 
    print("%d" % n + '\t'*2 + '%.2f' % f)

# Set the array size want to test
arr_size = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
# Print the title 
print("Array size\tRunning times(ms)")
# Run all array sizes
for i in range(0, len(arr_size)):
    result_fun(arr_size[i])

