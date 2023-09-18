import pandas as pd
ap = pd.read_csv('apple.csv')


##print(ap.head())
ap['Price1']=ap['Close'].shift(-1)
ap['PriceDiff'] = ap['Price1']-ap['Close']
ap['Direction'] = [1 if ap.loc[ei,'PriceDiff']>0 else -1
                   for ei in ap.index]
print(ap.head())
