import yfinance as yf
import talib as ta
print (dir(ta))
import pandas as pd
import matplotlib.pyplot as plt


power = yf.Ticker("POWERGRID.NS")
df = power.history(start="2020-01-01", end='2020-09-04')
df.head()


