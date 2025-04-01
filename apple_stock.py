import yfinance as yf

def fetch_apple_stock():
    # Create a Ticker object for Apple (AAPL)
    apple = yf.Ticker("AAPL")

    # Fetch historical stock data (e.g., last 1 month)
    data = apple.history(period="1mo")

    # Print date and closing price
    print("Apple Stock Prices (Last Month)")
    print("-" * 40)
    for date, row in data.iterrows():
        print(f"Date: {date.strftime('%Y-%m-%d')}, Close Price: ${row['Close']:.2f}")

if __name__ == "__main__":
    fetch_apple_stock()
