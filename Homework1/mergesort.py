###############################
## FIle name: mergesort.py
## Name: JIanglong Yu
## Date: 6/27
## descripution: This code will read a file with some numbers, then use merge sort to sort this number.
#################################

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

# print the list without '[]'
def print_arr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end = " ")

# read the file and print the sorted arr
def main_fun(filename):
    f = open(filename)
    for each_line in f:
        # this arr to store the arr from the text 
        arr = []
        # this arr1 to store the sort arr
        arr1 = []
        # get the number in a list
        arr.extend(each_line.strip().split(' '))
        # convert the string list into int list
        arr = list(map(int, arr))
        # delete the first element
        arr.pop(0)
        arr1 = mergesort(arr)
        print_arr(arr1)
        # change line 
        print("")

main_fun('data.txt')