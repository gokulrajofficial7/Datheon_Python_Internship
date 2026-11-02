# Task 2: Stock Portfolio Performance Tracker

## Overview
An investment portfolio valuation engine built in Python 3. Calculates real-time portfolio performance, percentage returns, weighted cost basis, and automatically persists transaction and holding summaries to `portfolio_summary.csv` using Python's built-in `csv` module.

---

## 🛠️ Key Features
- **Holdings Management:** Supports buying/adding positions (computes dynamic weighted average cost basis) and selling/removing positions.
- **Valuation Metrics:** Computes individual holding returns (%), total invested capital, current market value, and net unrealized P/L.
- **CSV Data Ingestion & Persistence:** Reads market reference prices from `constituents.csv` and writes summary records to `portfolio_summary.csv`.

---

## 🚀 How to Run
```bash
python portfolio.py
```
