import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt

#aapl = pdr.get_data_yahoo('AAPL', '2017-05-04')
closes = pd.DataFrame(aapl.Close)
#Moving Average for different number of days
closes['MA_9'] = closes.Close.rolling(9, center=True).mean()
closes['MA_21'] = closes.Close.rolling(21, center=True).mean()
closes['EMA'] = closes.Close.ewm(com=45).mean()
#Plot
plt.figure(figsize=(10,4))
plt.grid(True)
plt.plot(closes['Close'], label='AAPL')
plt.plot(closes['MA_9'], label='movingAverage 9')
plt.plot(closes['MA_21'], label='movingAverage 21')
plt.plot(closes['EMA'], label='EMA')
plt.legend(loc=2)
plt.savefig('AAPL.png')
