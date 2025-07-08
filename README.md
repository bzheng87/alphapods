# 📘 Alpha Pods – Take-Home Assignment

**Assignment**: CVaR-based Equity Strategy Optimization  
**Candidate**: Zech  
**Dates Covered**: 1 Jan 2010 – 31 Dec 2024  
**Universe**: 60 liquid U.S. stocks from the S&P 100  

---

## 🛠️ 1. Setup Instructions

### ✅ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### ✅ Install Required Packages

```bash
pip install -r requirements.txt
```

If missing, install manually:

```bash
pip install pandas numpy matplotlib seaborn cvxpy requests
```

---

## 📂 2. File Structure

```
quantprogram2025/
├── .ipynb_checkpoints/
│
├── part2/
│   ├── .ipynb_checkpoints/
│   ├── cumulative_strategy_returns.csv
│   ├── daily_strategy_returns.csv
│   ├── part2a.py
│   ├── part2b.py
│   ├── part2c.ipynb
│   ├── part2d.ipynb
│   ├── spx100_prices.csv
│   ├── ticker_industries.csv
│
├── venv/                        # (your Python virtual environment)
│
├── Alpha Pods-Home Assignment.pdf
├── api.json                    # removed
├── benchmarks.csv
├── cvar_index_quarterly_txn_cost.csv
├── cvar_index_values.csv
├── cvar_strategy_daily_returns.csv
├── part1.ipynb
├── README.md
├── requirements.txt
├── spx100_prices.csv
```

---

## 📊 3. Task A – Baseline CVaR Index

**Implemented in**: `part1.ipynb`

### ✔ Methodology

Optimized for **95% CVaR (Expected Shortfall)** under the following constraints:

- Fully invested (Σ weights = 1)  
- Long-only (no shorting)  
- Max 5% per stock  
- Quarterly rebalancing  
- Transaction Costs: 10 bps round-trip (5 bps in, 5 bps out)

### ✔ Benchmarks

- **Equal-Weighted SPX Portfolio** – proxied by `EQWL` ETF  
- **Market Cap-Weighted Benchmark** – proxied by `OEF` ETF

---

## 📈 4. Outputs (What to Submit)

| File                          | Description                                             |
|-------------------------------|---------------------------------------------------------|
| `daily_strategy_returns.csv`  | Daily returns for CVaR strategy and benchmarks          |
| `cumulative_strategy_returns.csv` | Cumulative performance (Growth of $1)              |
| `part1.ipynb`                 | CVaR logic, implementation, plots, summary table        |
| `part1.ipynb (Plot)`          | Visual comparison of strategy vs. EQWL and OEF          |
| `part1.ipynb (Table)`         | Annual return, volatility, Sharpe, CVaR, MDD, turnover  |

---

## 🧠 5. Part 2 – Alpha Enhancement

**Goal**: Improve the out-of-sample risk-adjusted performance of the baseline CVaR strategy using a sector-based alpha overlay.

### ✅ Methodology Summary

We enhanced the original CVaR index by incorporating sector-based signals.  
Each stock was tagged by sector using `ticker_industries.csv`.

Two overlay strategies were applied:

- **Momentum Overlay**: Allocate more weight to stocks in the best-performing sectors over the past quarter.  
- **Mean Reversion Overlay**: Allocate more weight to stocks in the worst-performing sectors, anticipating a reversal.

The models were evaluated **out-of-sample (Jan 2020 – Dec 2024)**.  
We also created a **combined strategy** to blend the two overlays for robustness.

### 🧠 Idea Type

- Alpha overlays based on **historical sector returns**  
- No ML/AI – just statistical + intuitive signals  
- Tactical tilts avoiding lookahead bias

---

## 📂 6. Files for Part 2

| File           | Description                                                                |
|----------------|----------------------------------------------------------------------------|
| `part2c.ipynb` | Momentum overlay: CVaR strategy tilted toward best-performing sectors      |
| `part2d.ipynb` | Mean Reversion overlay: CVaR strategy tilted toward worst-performing sectors |
