from this import d
import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

# important for setting start and end date later

today = date.today()

two_yrs_ago = today - relativedelta(years=2)

########

st.write("""
# Simple Stock Price App
### Shown are the stock **closing price** and ***volume*** of the stock of  your choosing!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
ticker_input = 'GOOGL'

user_ticker = st.text_input("Input Ticker Symbol", ticker_input.upper(), max_chars=5)
#get data on this ticker
ticker_data = yf.Ticker(user_ticker)

#
start_period = st.text_input("Select a start and end date timeframe you want to view (YYYY-MM-DD)", two_yrs_ago, max_chars=10)

end_period = st.text_input("Select a start and end date timeframe you want to view (YYYY-MM-DD)", today, max_chars=10)

st.write('''
***
''')

#get the historical prices for this ticker
tickerDf = ticker_data.history(period='7d', start=start_period, end=end_period)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(f"""
# Closing stock price for {user_ticker.upper()}.
""")

st.line_chart(tickerDf.Close, use_container_width=True)

st.write('''
***
''')


# setting pd DF in st
def get_stock_info(ticker_symbol):
  d = dict([
            ('Close',tickerDf.Close),
            ('Volume',tickerDf.Open),
            ('Dividends',tickerDf.Dividends)
            ])
  return d

X = get_stock_info(tickerDf)

X

dfp = pd.DataFrame.from_dict(d
, orient='index')
dfp = dfp.rename({0: '%'}, axis='columns')
dfp.reset_index(inplace=True)
dfp = dfp.rename(columns = {'index':'nucleotide'})
st.write(dfp)


ticker_data.financials

ticker_data.quarterly_financials