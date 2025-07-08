import requests
import pandas as pd
import json
import time

# Load API key
with open("../api.json", "r") as f:
    config = json.load(f)
API_KEY = config["fmp_api_key"]

# Full TICKERS list
TICKERS = [
    "AAPL","ABBV","ABT","ACN","ADBE","AIG","AMD","AMGN","AMT","AMZN","AVGO","AXP","BA",
    "BAC","BK","BKNG","BLK","BMY","BRK-B","C","CAT","CHTR","CL","CMCSA","COF","COP",
    "COST","CRM","CSCO","CVS","CVX","DE","DHR","DIS","DUK","EMR","FDX","GD","GE","GILD",
    "GM","GOOG","GOOGL","GS","HD","HON","IBM","INTC","INTU","ISRG","JNJ","JPM","KO","LIN",
    "LLY","LMT","LOW","MA","MCD","MDLZ","MDT","MET","META","MMM","MO","MRK","MS","MSFT",
    "NEE","NFLX","NKE","NOW","NVDA","ORCL","PEP","PFE","PG","PLTR","PM","PYPL","QCOM",
    "RTX","SBUX","SCHW","SO","SPG","T","TGT","TMO","TMUS","TSLA","TXN","UNH","UNP","UPS",
    "USB","V","VZ","WFC","WMT","XOM"
]

# To resume if partially completed
try:
    existing_df = pd.read_csv("ticker_industries.csv")
    fetched = set(existing_df["Ticker"])
    output = existing_df.to_dict("records")
    print(f"🔁 Resuming from previous data, {len(fetched)} tickers already fetched.")
except FileNotFoundError:
    fetched = set()
    output = []

# Loop with retry + sleep
for ticker in TICKERS:
    if ticker in fetched:
        continue

    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={API_KEY}"
    for attempt in range(3):  # up to 3 retries
        try:
            resp = requests.get(url)
            data = resp.json()
            if data and isinstance(data, list):
                info = data[0]
                output.append({
                    "Ticker": ticker,
                    "Company": info.get("companyName", ""),
                    "Sector": info.get("sector", ""),
                    "Industry": info.get("industry", "")
                })
                print(f"✅ {ticker}: {info.get('sector', '')} / {info.get('industry', '')}")
            else:
                print(f"⚠️ No data for {ticker}")
            break
        except Exception as e:
            print(f"❌ {ticker} attempt {attempt+1} failed: {e}")
            time.sleep(2)
    time.sleep(0.3)  # safe sleep (3–4 calls/sec)

# Save file
df = pd.DataFrame(output).drop_duplicates("Ticker")
df.to_csv("ticker_industries.csv", index=False)
print("\n✅ Finished saving ticker_industries.csv")
