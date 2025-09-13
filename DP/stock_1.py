prices=[7,10,1,3,6,9,2]

maxvalue=prices[-1]
profit=0
for i in range(len(prices)-2,-1,-1):
    profit=max(maxvalue-prices[i],profit)
    maxvalue=max(maxvalue,prices[i])

print(profit)