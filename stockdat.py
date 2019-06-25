from pandas_datareader import DataReader
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# pretty useful setting
style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

df = DataReader("TSLA", 'yahoo', start, end)

# operation in index and certain column
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

# -- read and save our data set
df.to_csv('TSLA.csv')
df = pd.read_csv('TSLA.csv')
df.index = pd.to_datetime(df['Date'])

# ----moving average
df['MA10'] = df.Close.rolling(window=10).mean()
df['MA20'] = df.Close.rolling(window=20).mean()



# plotting
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax1.plot(df.index, df.Close, label='Close price')
ax1.plot(df.index, df.MA10, label='MA10')
plt.legend(loc='upper right')

ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
ax2.bar(df.index, df.Volume, color='skyblue', label='Volume')
plt.legend()

# candle chart
df_ohlc = df['Adj Close'].resample('5D').ohlc()
df_volume = df['Volume'].resample('5D').sum()
df_ohlc = df_ohlc.reset_index()
df_ohlc.Date = df_ohlc.Date.map(mdates.date2num)

fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values,width=2,colorup='r',colordown='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
