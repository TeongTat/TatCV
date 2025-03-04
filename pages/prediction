import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(layout="wide")
st.title("Stock Price Prediction using ARIMA")

# User input for stock symbol
stock_symbol = st.text_input("Enter a stock symbol (e.g., AAPL, TSLA, MSFT):").upper()

# Ensure unique keys for date input fields
start_date = st.date_input("Start date for historical data", pd.to_datetime("2023-01-01"), key="start_date")
end_date = st.date_input("End date", pd.to_datetime("today"), key="end_date")

def fetch_stock_data(symbol, start, end):
    try:
        stock_data = yf.download(symbol, start=start, end=end)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# ✅ Assign a unique key to st.button()
if st.button("Predict", key="predict_button") and stock_symbol:
    st.subheader(f"Fetching Data for {stock_symbol}...")
    
    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)
    
    if stock_data.empty:
        st.error("No data found! Try selecting a different stock or date range.")
    else:
        st.write("Last 5 rows of historical data:")
        st.write(stock_data.tail())

        # Use 'Close', 'High', and 'Low' prices for forecasting
        stock_prices = stock_data[['Close', 'High', 'Low']].dropna()

        def train_arima(series):
            model = ARIMA(series, order=(5, 1, 0))
            return model.fit()

        model_close = train_arima(stock_prices['Close'])
        model_high = train_arima(stock_prices['High'])
        model_low = train_arima(stock_prices['Low'])

        # Forecast next 5 days
        forecast_close = model_close.forecast(steps=5)
        forecast_high = model_high.forecast(steps=5)
        forecast_low = model_low.forecast(steps=5)

        # Display predictions
        future_dates = pd.date_range(stock_prices.index[-1], periods=6)[1:]
        forecast_df = pd.DataFrame({
            'Date': future_dates, 
            'Predicted Close Price': forecast_close,
            'Predicted High Price': forecast_high,
            'Predicted Low Price': forecast_low
        })
        forecast_df.set_index("Date", inplace=True)

        st.subheader(f"Predicted {stock_symbol} Prices for Next 5 Days")
        st.write(forecast_df)

        # Plot results
        st.subheader(f"Predicted {stock_symbol} Chart:")
        fig, ax = plt.subplots(figsize=(10, 5))
        stock_prices['Close'][-50:].plot(ax=ax, label="Historical Close Prices", color="blue")
        forecast_df["Predicted Close Price"].plot(ax=ax, label="Forecast Close", linestyle="dashed", color="red")
        forecast_df["Predicted High Price"].plot(ax=ax, label="Forecast High", linestyle="dashed", color="green")
        forecast_df["Predicted Low Price"].plot(ax=ax, label="Forecast Low", linestyle="dashed", color="orange")
        ax.set_title(f"Stock Price Prediction for {stock_symbol}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
