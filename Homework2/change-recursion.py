# def recMC(coinValueList, change):
#     minCoins = change
#     if change in coinValueList:
#         return 1
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins = 1 + recMC(coinValueList, change-i)
#             if numCoins < minCoins:
#                 minCoins = numCoins
#         return minCoins

# print(recMC([1,5,10,25],63))

# def recDC(coinValueList, change, knownResults):
#     minCoins = change
#     if change in coinValueList:
#         knownResults[change] = 1
#         return 1
#     elif knownResults[change] > 0:
#         return knownResults[change]
#     else:
#         for i in [c for c in coinValueList if c <= change]:
#             numCoins = 1 + recDC(coinValueList, change-i, knownResults)
#             if numCoins < minCoins:
#                 minCoins = numCoins
#                 knownResults[change] = numCoins
#         return numCoins

# print(recDC([1,5,10,25],63,[0]*64))

#dynamic program
# def dpMC(coinValueList, change, minCoins):
#     for cents in range(1,change +1):
#         coinCount = cents
#         for j in [c for c in coinValueList if c <= cents]:
#             if minCoins[cents-j] + 1 < coinCount:
#                 coinCount = minCoins[cents-j] + 1
#         minCoins[cents] = coinCount
#     return minCoins[change]

# print(dpMC([1,5,10,21,25],63,[0]*64))

# def dpMC_P(coinValueList, change, minCoins, coinsUsed):
#     for cents in range(change + 1):
#         coinCount = cents
#         newCoin = 1
#         for j in [c for c in coinValueList if c <= cents]:
#             if minCoins[cents - j] + 1 < coinCount:
#                 coinCount = minCoins[cents - j] + 1
#                 newCoin = j
#         minCoins[cents] = coinCount
#         coinsUsed[cents] = newCoin
#     return minCoins[change]

# def printCoins(coinsUsed, change):
#     coin = change
#     while coin > 0:
#         thisCoin = coinsUsed[coin]
#         print(thisCoin)
#         coin = coin - thisCoin

# amnt = 63
# clist = [1,5,10,21,25]
# coinsUsed = [0] * (amnt +1)
# coinCount = [0] * (amnt + 1)
# print(dpMC_P(clist, amnt, coinCount, coinsUsed))
# printCoins(coinsUsed, amnt)
# print(coinsUsed)
