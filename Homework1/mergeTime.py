###############################
## FIle name: mergeTime.py
## Name: JIanglong Yu
## Date: 6/27
## descripution: This code will recording the time of merge sort to sort list with differet size.
#################################
import time
import random as r

## mergesort
def mergesort(arr):
    # set a function exit
    if len(arr) <= 1:
        return arr
    # set a middel point for using split the arr to two part
    flag = len(arr)//2
    # use the recursion function to split the arr constantly
    left_arr = mergesort(arr[:flag])
    right_arr = mergesort(arr[flag:])
    # set to pinter for compare the size of two numbers
    left_pointer = 0
    right_pointer = 0
    # set a arr to store the final array
    result_arr = []
    # when the pointer less then their length of arr, the left will compare their number contantly 
    while left_pointer < len(left_arr) and right_pointer < len(right_arr):
        # if left number less than right number, then put the left number into the result arr 
        if left_arr[left_pointer] < right_arr[right_pointer]:
            result_arr.append(left_arr[left_pointer])
            left_pointer += 1
        else:
            result_arr.append(right_arr[right_pointer])
            right_pointer += 1
    # once there is an arr's pointer greater than the length of the array, we can just put all elements 
    # of another array into the result arr 
    result_arr += left_arr[left_pointer:]
    result_arr += right_arr[right_pointer:]
    return result_arr

# Print running time and arr size
def result_fun(n):
    # Generates n numbers with a range of 0-10000 and put them into an arr 
    arr = r.choices(range(0,10000), k=n)
    # Start collecting time
    start = time.perf_counter()
    mergesort(arr)
    # End time
    end = time.perf_counter()
    # Convert the time unit from second to milisecond 
    f = (end-start) * 1000
    # Prin the array size and running time 
    print("%d" % n + '\t'*2 + "%.2f" % f)

# Set the array size want to test
arr_size = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,500000]
# Print the title 
print("Array size\tRunning times(ms)")
# Run all array sizes
for i in range(0, len(arr_size)):
    result_fun(arr_size[i])