# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def util_func(speed, E = 2.72, L = 1, k = 0.02, x0 = 175):
    return(L/(1+E**(-k*(speed -x0))))

speeds = np.arange(1001)
utils = util_func(speeds)

sns.scatterplot(data =df, x= 'mbps', y = 'utils')

df = pd.DataFrame({'mbps': speeds, 'utils': utils})
#df['mbps'] = df['mbps'].astype(str)


plt.scatter(df['mbps'], df['utils'])

prices = pd.read_csv('wifiPrices.csv')


plotdf = pd.merge(prices, df, left_on= 'mbps', right_on = 'mbps', how = 'left')

ax = sns.scatterplot(data=plotdf, x="price", y="utils", hue = 'company')
sns.regplot(data=plotdf, x="price", y="utils", scatter=False, ax = ax, ci = None)

sns.regplot