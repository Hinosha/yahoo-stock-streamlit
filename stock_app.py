import yfinance as yf
import streamlit as st
import pandas as pd

st.title("📈 Yahoo Stock Data Downloader")

ticker = st.selectbox("Select a stock ticker:", ['^GSPC', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'TSLA'])
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Fetch Data"):
    if start_date and end_date:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        if not data.empty:
            st.success("Data fetched successfully!")
            st.dataframe(data.head())
            csv = data.to_csv().encode('utf-8')
            st.download_button("Download CSV", csv, f"{ticker}_historical_data.csv", "text/csv")
        else:
            st.warning("No data available.")
    else:
        st.error("Please select both dates.")
