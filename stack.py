import pandas_datareader as pdr  
import datetime  
  
# 定义要下载的股票代码  
#ticker = 'AAPL'  
ticker = '600570'  
  
# 获取今天的日期，然后计算昨天的日期  
#today = datetime.date.today()  
#yesterday = today - datetime.timedelta(days=1)  

# 获取今天的日期，然后计算一年前的日期
today = datetime.date.today()
one_year_ago = today - datetime.timedelta(days=365)

# 使用pandas_datareader下载昨天的股票数据  
#stock_data = pdr.get_data_yahoo(ticker, yesterday, today)  

#stock_data = pdr.av.time_series.AVTimeSeriesReader(ticker, start=yesterday, end=today, api_key='YOUR_API_KEY').read()

#stock_data = pdr.quandl.QuandlReader(ticker, start=yesterday, end=today, api_key='YOUR_API_KEY').read()

# 使用pandas_datareader下载近一年的股票数据
stock_data = pdr.av.time_series.AVTimeSeriesReader(ticker, start=one_year_ago, end=today, api_key='YOUR_API_KEY').read()

# 打印数据  
#print(stock_data)
stock_data.to_excel('stock_data.xlsx')

import pandas as pd
# 读取 stock_data.xlsx 文件
#stock_data = pd.read_excel('stock_data.xlsx')

# 打印数据
print(stock_data)

import matplotlib.pyplot as plt

#print(stock_data.columns)
# 绘制周期为天的图表
plt.plot(stock_data.index, stock_data['close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Data')
plt.show()