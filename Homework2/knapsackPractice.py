# tr = {(10,20), (15,30), (22,22),(5,9), (4,7)}
# max_w = 20

# m = {}
# def KN(tr,w):
#     if tr == set() or w == 0:
#         m[tuple(tr), w] = 0
#         return 0;
#     elif (tuple(tr), w) in m:
#         return m[(tuple(tr), w)]
#     else:
#         vmax = 0
#         for t in tr:
#             if t[0] <= w:
#                 v = KN(tr-{t}, w-t[0])+t[1]
#                 vmax = max(vmax, v)
#         m[(tuple(tr),w)] = vmax
#         return vmax
    
# print(KN(tr,max_w))

# def Knapsack(items, W):
#     knapsackT = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]
#     for y in range(1, len(items) +1):
#         currentV = items[y-1][0]
#         currentW = items[y-1][1]
#         for x in range(W+1):
#             if x >= currentW:
#                 knapsackT[y][x] = max(knapsackT[y-1][x], knapsackT[y-1][x-currentW]+currentV)
#                 #KnapsackT[y][x] = max(knapsackT[y-1][x], knapsackT[y][x-currentW]+currentV)#完全背包问题
#             else:
#                 knapsackT[y][x] = knapsackT[y-1][x]
#     return knapsackT

# # 找到物品
# def finditem(table, items):
#     result = []
#     y = len(table)-1
#     x = len(table[0])-1
#     while x>0 and y>0:
#         if table[y][x] == table[y-1][x]:
#             y-=1
#         else:
#             result.append(y)
#             x -= items[y-1][1]
#             y-=1
#     result = list(reversed(result))
#     for i in range(len(result)):
#         print(result[i],end=" ")

# items = [[1,2], [4,3], [5,6], [6,7], [8,9]]
# W = 10
# table = Knapsack(items, W)
# w = table[-1][-1]
# finditem(table, items)

#使用一维数组不断刷新
# def KnapsackSuper(val,wt, W):
#     K_arr = [0 for _ in range(W+1)]
#     for x in range(1, len(val)+1):
#         for y in reversed(range(1, W+1)): # 改为for y in range(1, W+1) 变为完全背包问题
#             if (y >= wt[x-1]):
#                 K_arr[y] = max(K_arr[y], K_arr[y-wt[x-1]]+val[x-1])
#         print(K_arr)
#     return K_arr[W]

# wt = [2,3,4,7]
# val = [1,3,5,9]
# print(KnapsackSuper(val, wt, 10))


# # Dynamic programming solution
# def dp(val, wt, W, n):
#   # Creating an empty table
#   table = []
#   for x in range(n + 1):
#     table.append([])
    
#     for i in range(W + 1):
#       table[x].append(0)
      
#   fam = []
  
#   # Adding values into the table from the bottom up
#   for x in range(n + 1):
#     for y in range(W + 1):
#       if x == 0 or y == 0: # Set the values of the first row or column to 0
#         table[x][y] = 0
#       elif wt[x - 1] <= y: # Check if the weight of the nth item is less than the capacity of column y
#         # Finding the total weight when the nth item is added
#         # If the nth item helps increase the total weight without exceeding the max weight, it will be added.
#         # Otherwise, it will not be included
#         if table[x - 1][y] < val[x - 1] + table[x - 1][y - wt[x - 1]]:
#           table[x][y] = val[x - 1] + table[x - 1][y - wt[x - 1]]
#         else:
#           table[x][y] = table[x - 1][y]
#       else:
#         table[x][y] = table[x - 1][y] # Setting the current value with the previous one
  
#   maxWeight = table[n][W]
#   temp = W
  
#   # Printing the items needed to get the max weight
#   for x in range(n, 0, -1):
#     # Checking if the value is included in the max weight
#     if maxWeight > 0 and maxWeight != table[x - 1][temp]:
#       fam.append(x)
      
#       # Reducing the total weight
#       maxWeight -= val[x - 1]
#       temp -= wt[x - 1]
  
#   fam.sort() # Sorting the order of the items
#   fam.insert(0, table[n][W]) # Adding the max weight to the beginning of the list
  
#   # Return the maximum possible weight
#   return fam

# # Open data.txt file
# fileText = open('shopping.txt', 'r')
# text = fileText.readlines()

# testCases = int(text[0]) # Getting the number of test cases
# line = 1

# # Going through all of the test cases
# for x in range(testCases):
#   val = []
#   wt = []
#   W = []
#   n = int(text[line]) # Getting the number of items
#   line += 1
  
#   # Getting the values and weights of each item
#   for i in range(n):
#     arr = text[line].split()
#     val.append(int(arr[0]))
#     wt.append(int(arr[1]))
#     line += 1

#   F = int(text[line]) # Getting the number of family members
#   line += 1
#   ans = []
#   total = 0
  
#   # Getting the total price of all goods that the entire family and each family member can carry out during their shopping spree
#   for i in range(F):
#     W = int(text[line])
#     line += 1
#     ans.append(dp(val, wt, W, n))
#     total += ans[i][0]
  
#   # Printing the total price as well as the items each family member can get
#   print("Test Case", x + 1)
#   print("Total Price", total)
  
#   # Printing the individual items
#   for i in range(F):
#     print(str(i + 1) + ": ", end='')
    
#     for j in range(1, len(ans[i])):
#       print(ans[i][j], end=' ')
    
#     print()
  
#   print()