###############################
## FIle name: insertsort.py
## Name: JIanglong Yu
## Date: 6/27
## descripution: This code will read a file with some numbers, then use insert sorting to sort these number.
#################################

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
        # get the number in a list
        arr.extend(each_line.strip().split(' '))
        # convert the string list into int list
        arr = list(map(int, arr))
        # delete the first element
        arr.pop(0)
        insertsort(arr)
        print_arr(arr)
        # change line 
        print("")

main_fun('data.txt')