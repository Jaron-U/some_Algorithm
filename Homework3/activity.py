###############################
## FIle name: activity.py
## Name: Jianglong Yu
## Date: 7/20
## descripution: This code is read the file, and deal with these data
#################################
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

def printActivities(s , f, act_n):
    # set a tuple to store the activities
    selected = []
    # put the index of acitvities, start time, and finish time into a tuple
    act_tuple = list(zip(act_n, s, f))
    # sort by start time in this tuple
    #act_tuple.sort(key = lambda x : x[1])
    act_tuple = insertsort(act_tuple)
    # get the size of the tuple
    n = len(act_tuple)
    # set the index of start loop
    i = n-1
    # Becasue we find the result from the last start time, so the results should have the last start activities
    selected.append(act_tuple[i])
    # create the num_activity to record the maximum number of activity 
    num_activity = 1
    # for loop begin with the last element in the tuple
    for j in reversed(range(0, i)):
        # if the finish time of current acivity is less equal than beign time of the last activity
        if act_tuple[j][2] <= act_tuple[i][1]:
            # we just add this activity into our result list
            selected.append(act_tuple[j])
            num_activity += 1
            # we set the current activity as the last activity for next loop
            i = j
    print("Maximum number of activities =", num_activity)
    # the result we get is descending, we need reversed them and print out
    selected = tuple(reversed(selected))
    print("", end =" ")
    for i in range(0, len(selected)):
        print(selected[i][0], end = " ")
    print("")

# print the result to terminal
def printresult(filename):
    fe = open(filename)
    # read each line in to a list
    lines = fe.readlines() 
    max_line = len(lines)
    # set a line flag
    line_idx = 0
    # get the number of activies
    n_act = int(lines[line_idx])
    set_num = 0
    while 1:
        set_num += 1
        # start time list
        s = []
        # finish time list
        f = []
        # activiy index
        act_idx = []
        line_idx += 1
        for _ in range(n_act):
            act_info = []
            # get these number in this line, put them into a list
            act_info.extend(lines[line_idx].strip().split(' '))
            # convert the string list into int list
            act_info = list(map(int, act_info))
            act_idx.append(act_info[0])
            s.append(act_info[1])
            f.append(act_info[2])
            line_idx += 1
        print("Set", set_num)
        printActivities(s , f, act_idx)
        print("")
        # if the line index is greater than the lines of this file, just break
        if line_idx < max_line:
            n_act = int(lines[line_idx])
        else:
            break
        
    fe.close()

printresult("act.txt")