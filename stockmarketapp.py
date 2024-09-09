import streamlit as st
import yfinance as yf
import datetime

ticker_symbol = st.text_input("Enter the  stock", "AAPL")
start_date = st.date_input("start_date", datetime.date(2019, 7, 6))
end_date = st.date_input("end_date", datetime.date(2023, 1, 7))

data=yf.download(ticker_symbol,start=start_date,end=end_date)

st.write(data)

st.line_chart(data["Close"])
st.bar_chart(data["Volume"])
