import requests
import pandas as pd
import json
import time

# Load API key
with open("../api.json", "r") as f:
    config = json.load(f)
API_KEY = config["fmp_api_key"]

# Tickers list (already defined)
TICKERS = [
    "AAPL","ABBV","ABT","ACN","ADBE","AIG","AMD","AMGN","AMT","AMZN","AVGO","AXP","BA",
    "BAC","BK","BKNG","BLK","BMY","BRK.B","C","CAT","CHTR","CL","CMCSA","COF","COP",
    "COST","CRM","CSCO","CVS","CVX","DE","DHR","DIS","DUK","EMR","FDX","GD","GE","GILD",
    "GM","GOOG","GOOGL","GS","HD","HON","IBM","INTC","INTU","ISRG","JNJ","JPM","KO","LIN",
    "LLY","LMT","LOW","MA","MCD","MDLZ","MDT","MET","META","MMM","MO","MRK","MS","MSFT",
    "NEE","NFLX","NKE","NOW","NVDA","ORCL","PEP","PFE","PG","PLTR","PM","PYPL","QCOM",
    "RTX","SBUX","SCHW","SO","SPG","T","TGT","TMO","TMUS","TSLA","TXN","UNH","UNP","UPS",
    "USB","V","VZ","WFC","WMT","XOM"
]

START_DATE = "2010-01-01"
END_DATE = "2024-12-31"

def fetch_data(ticker):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={START_DATE}&to={END_DATE}&apikey={API_KEY}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json().get("historical", [])
        if data:
            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["date"])
            df = df.set_index("date").sort_index()
            return df["adjClose"]
        else:
            print(f"⚠️ No data for {ticker}")
            return pd.Series(dtype=float)
    except Exception as e:
        print(f"❌ Failed for {ticker}: {e}")
        return pd.Series(dtype=float)

# Download and merge all tickers into one DataFrame
price_data = {}

for ticker in TICKERS:
    print(f"📥 Fetching {ticker}")
    price_data[ticker] = fetch_data(ticker)
    time.sleep(0.3)  # respect rate limits

# Combine into a single DataFrame
df_all = pd.DataFrame(price_data)
df_all.to_csv("spx100_prices.csv", index_label="Date")
print("✅ Done! Saved to spx100_prices.csv")
