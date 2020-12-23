
import requests

ticker = 'SQ'
time_interval = '5min'

def compute(cur_val):
    # preform SMA calc
    return cur_val + 15

def main():
    request_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=' + time_interval + '&apikey=PKM3CD99R0XVSDYL4T48'
    request = requests.get(request_URL)
    last_refreshed = request.json()['Meta Data']['3. Last Refreshed']
    ts = request.json()['Time Series (' + time_interval + ')'][last_refreshed]
    val = float(ts['4. close'])
    print(compute(val))


if __name__ == '__main__':
    main()



# ts = TimeSeries(key = api_key, output_format = 'pandas')
# data_ts, meta_data_ts = ts.get_intraday(symvol='MSFT', interval = '1min', outputsize ='full')
#
# period = 60
#
# ti = TechIndicators(key=api_key, output_format='pandas')
# data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min',
#                          time_period=period, series_type='close')
#
#
# df1 = data_ti
# df2 = data_ts['4. close'].iloc[periods-1::]
#
# print(df1)
# df2.index = df1.index
# print(df2)
#
# total_df = pd.concat([df1,df2], axis=1)
# print(total_df)
#
# total_df.plot()
# plt.show()
