Alpha Pods – Take-Home Assignment

Assignment: CVaR-based Equity Strategy Optimization
Candidate: Zech
Dates Covered: 1 Jan 2010 – 31 Dec 2024
Universe: 60 liquid U.S. stocks from the S&P 100


# 📘 Alpha Pods – Take-Home Assignment

**Assignment:** CVaR-based Equity Strategy Optimization  
**Candidate:** Zech  
**Dates Covered:** 1 Jan 2010 – 31 Dec 2024  
**Universe:** 60 liquid U.S. stocks from the S&P 100  

---

## 🛠️ 1. Setup Instructions

### ✅ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

✅ Install Required Packages
pip install -r requirements.txt

If missing, install manually:

pip install pandas numpy matplotlib seaborn cvxpy requests

### 📂 2. File Structure

├── part1.ipynb              # Data load, ticker mapping, setup
├── part2a.py                # Industry/sector data from FMP API
├── part2b.py                # Historical price data from FMP API
├── part2c.ipynb              # Momentum vs Mean Reversion strategy
├── part2d.ipynb              # ⚠️ Core CVaR strategy implementation (Task A)
├── ticker_industries.csv    # Ticker-sector mapping (from part2a.py)
├── spx100_prices.csv        # Daily prices (from part2b.py)
├── daily_strategy_returns.csv
├── cumulative_strategy_returns.csv


### 📊 3. Task A – Baseline CVaR Index
Implemented in: part1.ipynb

✔ Methodology
Optimized for 95% CVaR (Expected Shortfall)


Constraints:
Fully invested (Σ weights = 1)
Long-only (no shorting)
Max 5% per stock
Quarterly rebalancing
Transaction Costs: 10 bps round-trip (5 bps in, 5 bps out)

### ✔  Benchmarks
Equal-Weighted SPX Portfolio – proxied by EQWL ETF
Market Cap-Weighted Benchmark – proxied by OEF ETF

### 📈 4. Outputs (What to Submit)
File	Description
daily_strategy_returns.csv	Daily returns for CVaR strategy and benchmarks
cumulative_strategy_returns.csv	Cumulative performance (Growth of $1)
part1.ipynb	CVaR strategy logic and implementation
part1.ipynb	Generates performance plot and summary table
part1.ipynb Plot	Visual comparison of strategy vs. EQWL and OEF
part1.ipynb Table	Annual return, volatility, Sharpe, CVaR, MDD, turnover


### 📈 Part 2 – Alpha Enhancement
Goal: Improve the out-of-sample risk-adjusted performance of the baseline CVaR strategy using a sector-based alpha overlay.

### ✅ Methodology Summary
We enhanced the original CVaR index by incorporating sector-based signals:

All stocks were tagged by sector using ticker_industries.csv.

We implemented two overlay strategies:

Momentum Overlay: Allocate more weight to stocks in the best-performing sectors over the past quarter.

Mean Reversion Overlay: Allocate more weight to stocks in the worst-performing sectors, anticipating a reversal.

The strategies were evaluated and compared out-of-sample from Jan 2020 – Dec 2024.

Final results include a combined strategy, blending both overlays for robustness.

### 🧠 Idea Type
Alpha Overlays using historical sector returns:

No ML/AI used—statistical and intuitive signals only.

Tactical tilt based on simple historical performance, avoiding lookahead bias.

### 📂 Files
File	Description
part2c.ipynb	Momentum strategy: CVaR strategy overlaid with top sector allocation
part2d.ipynb	Mean reversion strategy: CVaR strategy tilted toward worst-performing sectors
