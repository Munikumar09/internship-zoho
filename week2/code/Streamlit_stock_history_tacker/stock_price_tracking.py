import streamlit as st
import yfinance as yf

st.write(
    """ 
    # Stock Price App
    This app shows the **closing price** and **volume** 
    """
)
ticker_symbol = st.text_input("enter stock symbol listed in NSE or BSE")
st.write(
    """for NSE append the `.NS` to stock symbol, for BSE append the `.BO` to stock symbol"""
)
ticker_data = yf.Ticker(ticker_symbol)
info = ticker_data.info
if not info["regularMarketPrice"] == None:
    ticker_df = ticker_data.history(period="1d", start="2010-10-05", end="2022-11-04")
    st.write(
        """ 
    ## Daily closing price chart
    """
    )
    st.line_chart(ticker_df.Close)
    st.write(
        """ 
    ## Daily volume chart
    """
    )
    st.bar_chart(ticker_df.Volume)
else:
    st.write("""Stock not found Pleas enter correct symbol and extension""")
