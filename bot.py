import datetime
import requests

def run_trading_bot():
    print(f"[{datetime.datetime.now()}] Running Forex Market Analysis Bot...")
    
    # Example Market Data fetch using Free Open API
    try:
        url = "https://open.er-api.com/v6/latest/EUR"
        response = requests.get(url).json()
        usd_rate = response['rates']['USD']
        print(f"Current EUR/USD Rate: {usd_rate}")
        
        # Simple Strategy Condition Test
        if usd_rate > 1.05:
            print("Signal: Bullish Trend Detected")
        else:
            print("Signal: Bearish / Range Trend Detected")
            
    except Exception as e:
        print("Error fetching market data:", e)

if __name__ == "__main__":
    run_trading_bot()
