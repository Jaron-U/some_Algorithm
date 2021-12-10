def printMaxActivities(s , f, act_n):
    selected = []
    tuple1 = list(zip(act_n, s, f))
    # sort by start time in this tuple
    tuple1.sort(key = lambda x : x[1])
    # reversed this tuple, becasue we need find the result from the last start time
    n = len(tuple1)
    i = n-1
    selected.append(tuple1[i])
    num_activity = 1
    for j in reversed(range(0, i)):
        if tuple1[j][2] <= tuple1[i][1]:
            selected.append(tuple1[j])
            num_activity += 1
            i = j
    print("Maximum number of activities = ", num_activity)
    selected = tuple(reversed(selected))
    for i in range(0, len(selected)):
        print(selected[i][0], end = " ")

def insertsort(tuple1):
    for i in range(1, len(tuple1)):
        # temp is insertion element
        temp = tuple1[i]
        j = i
        # when the j is greater than 0 and the insertion element is less than the left element, 
        # they will swap the position constantly.
        while j > 0 and temp[1] < tuple1[j-1][1]:
            tuple1[j] = tuple1[j-1]
            tuple1[j-1] = temp
            j -= 1
    return tuple1

# Driver code
# Activity = [[1,4],[3,5],[0,6],[5,7],[3,9],[4,9],[6,10],[9,11],[8,12],[2,14],[12,16]]
s = [1,3,0,5,3,4,6,9,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]
act_n = [1,2,3,4,5,6,7,8,9,10,11]
tuple1 = list(zip(act_n, s, f))
print(insertsort(tuple1))
# s = [6,7,1]
# f = [8,9,2]
# act_n = [3,1,2]
# print("Set 1")
# printMaxActivities(s, f, act_n)
