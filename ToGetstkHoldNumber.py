import tushare

def toGetStoHoldNumber(ticker,folder):
    # Step 1. Get intraday data online
    pro = tushare.pro_api('2ed1d88c7027a80b8ff96ce6b60ae39b5b84bbc92845d2a474eb1540')
    df = pro.stk_holdernumber(ts_code='300199.SZ', start_date='20160101', end_date='20181231')

    print(df)


    # Step 2. If the history exists, append
    file = folder + '/' + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    # Step 3. Inverse based on index
    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'

    # Step 4. Save
    intraday.to_csv(file)
    print('Intraday for [' + ticker + '] got.')