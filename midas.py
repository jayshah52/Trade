import numpy as np
import pandas
from pandas import DataFrame
def generate():
    #generating an array that has a rateofchangeofprice with mean of 0 and std deviation of 0.1
    rateofchangeofprice = np.random.normal(loc = 0, scale = 0.1, size = 1000)

    #Creating a prices array First value is 1.0
    price = [1.0]*len(rateofchangeofprice)

    #Iterating to fill the prices array with formula
    #(price(t+1) - price(t))/ price(t) = arr[i]
    for i in range(1,len(rateofchangeofprice)):
        price[i] = rateofchangeofprice[i-1]*price[i-1] + price[i-1]

    #Creating a dataframe with pandas using a dictionary
    di = {"price":price}
    df = DataFrame(di)
    #print(df)
    return price,df

for val in [1,10,100,1000]:
    arr = []
    brokecounter = 0
    counter = 100
    while counter:
        prices, df = generate()
        profit = 0
        purchase = []
        currentunits = len(purchase)
        i = 0
        x = val
        while x > 0 and i < len(prices)-1:
            if currentunits > 0:
                if prices[i+1] - prices[i] < -0.01:
                    purchase.append(prices[i+1])
                    x -= prices[i+1]


                elif prices[i+1] - prices[i] > 0.11:
                    profit += prices[i+1]*len(purchase) - sum(purchase)
                    purchase = []

            elif currentunits == 0:
                if prices[i+1] > prices[i]:
                    purchase.append(prices[i+1])
                    x -= prices[i+1]

            if x <= 0:
                brokecounter += 1

            i += 1
            currentunits = len(purchase)

        arr.append(profit)
        counter -= 1
    narr = np.array(arr)
    meanprofit = np.mean(narr)
    profitpercent = (meanprofit/val)*100
    print(f' %Profit: {profitpercent}')
    print(f' You go broke {brokecounter} out of  100 times')
