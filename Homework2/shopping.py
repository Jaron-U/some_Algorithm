###############################
## FIle name: shopping.py
## Name: Jianglong Yu
## Date: 7/13
## descripution: This code is read the file, and deal with these data
#################################

# kanapsack function use dynamic programming algorithm
def KnapsackDP(val, wt, W):
    # get the item number
    n_items = len(val)
    # generate a Table
    knapsackT = [[0 for _ in range(W + 1)] for _ in range(n_items + 1)]
    # Then we need put the values into this table
    for i in range(1, n_items + 1):
        for j in range(1, W+1):
            # if current weigth of the item is greater than the current knapsack Capacity,
            if j < wt[i-1]:
                # this value will equal the last item in this weigth column 
                knapsackT[i][j] = knapsackT[i-1][j]
            else:
                # If current items can be put into the knapsack, we need decide which way has the maximum value
                knapsackT[i][j] = max(knapsackT[i-1][j], knapsackT[i-1][j-wt[i-1]]+val[i-1])
    # return the last value
    return knapsackT

# print items that person took
def finditem(table, wt):
    result = []
    # y is the item, x is the W
    y = len(table)-1
    x = len(table[0])-1
    while x>0 and y>0:
        # in the some column, if we find the the value item y is equal to value of item y-1. 
        # mean we did not take the items y. 
        if table[y][x] == table[y-1][x]:
            # just keep searching.
            y-=1
        else:
            # if not equal, mean is we take this item, just add the index of this item into the list
            result.append(y)
            # minus the wigth of this item.
            x -= wt[y-1]
            y-=1
    # reverse this list
    result = list(reversed(result))
    # print the list one by one
    for i in range(len(result)):
        print(result[i],end=" ")

# print the result to terminal
def printresult(filename):
    f = open(filename)
    # read each line in to a list
    lines = f.readlines()
    # get the number of test case, use int that convert the str into int
    case_num = int(lines[0])
    # set a line flag
    line_idx = 1
    # for loop the test case and print result
    for T in range(case_num):
        # init the price of item is P and weigth of item is W 
        P = []
        W = []
        # put he family number's "capacity" into the list
        FM = []
        # get the number of items 
        N = int(lines[line_idx])
        line_idx += 1
        # use for loop to get the item_info
        for _ in range(N):
            item_info = []
            item_info.extend(lines[line_idx].strip().split(' '))
            # convert the string list into int list
            item_info = list(map(int, item_info))
            P.append(item_info[0])
            W.append(item_info[1])
            line_idx += 1
        # get the number of peopel in family
        F = int(lines[line_idx])
        line_idx += 1
        total_price = 0
        # print the Test case
        print("Test Case %d" %(T+1))
        # get the capcity of every family member and total price
        for i in range(F):
            FM.append(int(lines[line_idx]))
            FM = list(map(int, FM))
            table = KnapsackDP(P, W, FM[i])
            total_price += table[-1][-1]
            line_idx += 1
        # print the total price
        print("Total Price %d" %total_price)
        # print the items
        for i in range(F):
            # print the index of member
            print(i+1, end=": ")
            table = KnapsackDP(P, W, FM[i])
            # print the items index
            finditem(table, W)
            print("")
        # change line
        print("")
    f.close()

printresult("shopping.txt")