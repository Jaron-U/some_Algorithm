###############################
## FIle name: Knapsack.py
## Name: Jianglong Yu
## Date: 7/13
## descripution: this code is collect the running time of DP and Rec algorithm.
#################################
import time
import random as r

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
    return knapsackT[-1][-1]

# kanapsack function use recursion without memo
def KnapsackRC(val, wt, W, n_item):
    # base case
    if (n_item == 0 or W == 0):
        return 0
    # if the current weight of item is greater than the knapsack capacity
    elif (wt[n_item-1] > W):
        # we just check the next item
        return KnapsackRC(val, wt, W, n_item-1)
    else:
        # we should decide put this item or not
        return max(KnapsackRC(val, wt, W, n_item-1), val[n_item-1] + KnapsackRC(val, wt, W-wt[n_item-1], n_item-1))

def result(x,c):
    # set the size of first list 
    n = 10
    # set the capacity of knapsack
    W = 100
    # creat x wt and val list with random number
    for _ in range(x):
        # generate the val list
        val = r.sample([k for k in range(50,150)], n)
        # generate the weight list
        wt = r.sample([j for j in range(1,100)], n)

        # Start collecting time of DP
        DPstart = time.perf_counter()
        max_DP = KnapsackDP(val, wt, W)
        # End time
        DPend = time.perf_counter()
        # Convert the time unit from second to milisecond 
        DP_time = (DPend-DPstart) * 1000
        # keep 6 signicicant figures
        DP_time = format(DP_time, '.3f')

        # Start collecting time of RC
        RCstart = time.perf_counter()
        max_RC = KnapsackRC(val, wt, W, n)
        # End time
        RCend = time.perf_counter()
        # Convert the time unit from second to milisecond 
        RC_time = (RCend-RCstart) * 1000
        # keep 6 signicicant figures
        RC_time = format(RC_time, '.3f')
        
        # output
        print("N =", n, " W =", W, " Rec time =", RC_time, " DP time =", DP_time, " max Rec =", max_RC, " max DP =", max_DP)
        if c == 0:
            #if c=0, W will not change, N will add 5 each time
            n += 5
        else:
            #if c=1, N wll not change, W will add 100 each time
            W += 100

# generate 7 lines data
x = 7
# set W is constant equal 100, N is increasing
result(x,0)
