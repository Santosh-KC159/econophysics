import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apple = pd.read_csv('AAPL.csv')
opens = np.array(apple['Open'])

def movingAverage(signal, window=40):
    kernelSize = window
    kernelArr = np.arange(0, kernelSize)
    kernel = np.exp(kernelArr)
    kernel = kernel/np.max(kernel)
    #weight = np.repeat(1.0, window)/window
    sma = np.convolve(signal, kernel, 'valid')
    return sma

convs = movingAverage(opens, window=40)
plt.figure(figsize=(10,5))
plt.plot(opens)
plt.plot(convs)
window = 30
weight = np.repeat(1.0, window)/window
weight
