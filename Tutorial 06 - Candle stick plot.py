import pandas
import matplotlib
# import matplotlib.finance
# from matplotlib import finance
import mpl_finance
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')
#matplotlib.style.use('dark_background')

def stockPricePlot(ticker):
	print(matplotlib.__version__)
	# Step 1. Load Data
	history = pandas.read_csv('../02 StockData/01 IntradayCN/'+ticker+'.csv', parse_dates=True, index_col=0)

	# Step 2. Data Manipulation
	close = history['close']
	close = close.reset_index()  #索引列
	close['timestamp'] = close['timestamp'].map(matplotlib.dates.date2num) #映射

	ohlc = history[['open', 'high', 'low', 'close']].resample('1H').ohlc() #重新采样 1h
	ohlc = ohlc.reset_index()
	ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)

	# Step 3. Plot Figures. Subplot 1: scatter plot. Subplot 2: candle stick plot.
	# Step 3.1. Subplot 1: scatter plot
	subplot1 = plt.subplot2grid((2,1), (0,0), rowspan=1, colspan=1)
	subplot1.xaxis_date()
	subplot1.plot(close['timestamp'], close['close'], 'b.')
	plt.title(ticker)

	# Step 3.2. Subplot 2: candle stick plot
	subplot2 = plt.subplot2grid((2,1), (1,0), rowspan=1, colspan=1, sharex=subplot1)
	mpl_finance.candlestick_ohlc(ax=subplot2, quotes=ohlc.values, width=0.01, colorup='g', colordown='r')# 宽度 上升期 下降期
	plt.show()

stockPricePlot('600031')