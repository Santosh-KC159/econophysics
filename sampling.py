import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

style.use('ggplot')

'''
start = dt.datetime(2015,1,1)
end = dt.datetime(2019,12,31)
df = web.DataReader('TSLA', 'yahoo', start, end)
df.to_csv('tesla.csv')
'''
name = 'AAPL'
df = pd.read_csv('data/{}.csv'.format(name), parse_dates=True, index_col=0)
df['100MA'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()
df_ohlc = df['Adj Close'].resample('10D').ohlc()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan=1, sharex= ax1)


ax1.plot(df.index, df['Adj Close'], linewidth=0.5, color='blue', label='Adj Close')
ax1.plot(df.index, df['100MA'], color='red', label='EMA')
plt.legend(loc=2)

ax2.bar(df.index, df['Volume'], label='Volume')
plt.legend(loc=2)
plt.savefig('{}.png'.format(name))
plt.show()
