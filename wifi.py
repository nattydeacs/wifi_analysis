# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300


def util_func(speed, E = 2.72, L = 1, k = 0.02, x0 = 250):
    return(L/(1+E**(-k*(speed -x0))))

speeds = np.arange(1001)
utils = util_func(speeds)

df = pd.DataFrame({'mbps': speeds, 'utils': utils})

#############################################
#Utils Plot
#############################################

NDColors = ["#B0C0BF", "#332A21", "#64A1B4",
              "#AE8988", "#C36733", "#DD7764", 
              "#602A10"]

fig = sns.lineplot(data =df, x= 'mbps', y = 'utils', color='#64A1B4', linewidth = 2.5)
sns.set_style("white")
sns.despine()
plt.xlabel("Internet Speed (mbps)")
plt.ylabel("Customer's Utility (0-1 scale)")
plt.title("Faster Internet speeds increase utility rapidly up to ~250mbps but plateau around 350mbps")

#############################################
#Best Internet Plot
#############################################

prices = pd.read_csv('wifiPrices.csv')
plotdf = pd.merge(prices, df, left_on= 'mbps', right_on = 'mbps', how = 'left')


fig2 = sns.scatterplot(data=plotdf, x="price", y="utils", hue = 'company', 
                       palette=(['#6460AC', '#ed1c24', '#46b555']))
sns.regplot(data=plotdf, x="price", y="utils", scatter=False, ax = fig2, ci = None, 
            color= 'black', line_kws={'linewidth':.6})
plt.xlabel("Price/month ($USD)")
plt.ylabel("Customer's Utility (0-1 scale)")
plt.title("The Astound 600mbps plan is the best deal")
for i in range(plotdf.shape[0]):
 plt.text(x=plotdf.price[i]-1.5,y=plotdf.utils[i]-.05,s=str(plotdf.mbps[i])+'mbps', 
          fontdict=dict(color='black',size=5.8))
 


str(plotdf.mbps[1])+'mbps'
