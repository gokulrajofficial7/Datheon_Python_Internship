"""
Datheon Python Programming Internship - Task 2
Stock Portfolio Performance Tracker

Features:
- Track stock ticker positions: Shares, Buy Price, Current Price
- Calculate Total Invested Capital, Current Market Value, Gain/Loss ($), and Return (%)
- Reference market data from 'constituents.csv'
- Persist portfolio valuation and performance audit to 'portfolio_summary.csv' using Python's csv module
"""

import csv
import os
import sys
from datetime import datetime

DEFAULT_PRICES = {
    "AAPL": 180.50,
    "MSFT": 420.25,
    "GOOGL": 175.80,
    "AMZN": 185.30,
    "TSLA": 250.40,
    "NVDA": 130.60,
    "META": 560.10,
    "JPM": 220.00,
    "NFLX": 690.00,
    "DIS": 95.50
}


class PortfolioTracker:
    def __init__(self, data_file="constituents.csv", output_file="portfolio_summary.csv"):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(self.base_dir, data_file)
        self.output_file = os.path.join(self.base_dir, output_file)
        self.market_prices = dict(DEFAULT_PRICES)
        self.holdings = {}  # ticker -> {'shares': int, 'buy_price': float}

        self.load_market_prices()
        self.seed_sample_holdings()

    def load_market_prices(self):
        """Loads latest market prices from constituents.csv if available."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, mode="r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        symbol = row.get("Symbol", "").strip().upper()
                        price = row.get("CurrentPrice", "")
                        if symbol and price:
                            self.market_prices[symbol] = float(price)
            except Exception as e:
                print(f"[Notice] Using default market feeds: {e}")

    def seed_sample_holdings(self):
        """Pre-seeds standard sample investment holdings for demo purposes."""
        self.holdings["AAPL"] = {"shares": 15, "buy_price": 165.00}
        self.holdings["NVDA"] = {"shares": 30, "buy_price": 110.00}
        self.holdings["TSLA"] = {"shares": 10, "buy_price": 265.00}
        self.holdings["MSFT"] = {"shares": 8, "buy_price": 395.50}

    def add_position(self, ticker, shares, buy_price):
        """Adds or updates an equity position in the portfolio."""
        ticker = ticker.strip().upper()
        if not ticker:
            raise ValueError("Ticker symbol cannot be empty.")
        if shares <= 0:
            raise ValueError("Shares quantity must be positive.")
        if buy_price <= 0:
            raise ValueError("Buy price must be positive.")

        if ticker in self.holdings:
            # Calculate weighted average cost basis
            existing = self.holdings[ticker]
            total_shares = existing["shares"] + shares
            total_cost = (existing["shares"] * existing["buy_price"]) + (shares * buy_price)
            new_avg_price = total_cost / total_shares
            self.holdings[ticker] = {"shares": total_shares, "buy_price": round(new_avg_price, 2)}
            print(f"[Updated] Added {shares} shares to '{ticker}'. New position: {total_shares} @ ${new_avg_price:.2f}")
        else:
            self.holdings[ticker] = {"shares": shares, "buy_price": buy_price}
            print(f"[Added] Position in '{ticker}': {shares} shares @ ${buy_price:.2f}")

        # If ticker is not in market_prices, default to buy_price
        if ticker not in self.market_prices:
            self.market_prices[ticker] = buy_price

    def remove_position(self, ticker):
        """Removes an equity position from holdings."""
        ticker = ticker.strip().upper()
        if ticker in self.holdings:
            del self.holdings[ticker]
            print(f"[Success] Removed '{ticker}' from portfolio.")
            return True
        print(f"[Error] Ticker '{ticker}' not found in portfolio.")
        return False

    def get_portfolio_metrics(self):
        """Computes comprehensive portfolio valuation metrics."""
        summary_rows = []
        total_invested = 0.0
        total_market_value = 0.0

        for ticker, data in self.holdings.items():
            shares = data["shares"]
            buy_price = data["buy_price"]
            curr_price = self.market_prices.get(ticker, buy_price)

            invested = shares * buy_price
            market_val = shares * curr_price
            gain_loss = market_val - invested
            pct_return = (gain_loss / invested * 100.0) if invested > 0 else 0.0

            total_invested += invested
            total_market_value += market_val

            summary_rows.append({
                "Ticker": ticker,
                "Shares": shares,
                "BuyPrice": buy_price,
                "CurrentPrice": curr_price,
                "InvestedCapital": invested,
                "CurrentValue": market_val,
                "GainLoss": gain_loss,
                "ReturnPct": pct_return
            })

        total_gain_loss = total_market_value - total_invested
        total_pct_return = (total_gain_loss / total_invested * 100.0) if total_invested > 0 else 0.0

        return summary_rows, total_invested, total_market_value, total_gain_loss, total_pct_return

    def display_portfolio(self):
        """Prints a clean tabular valuation report to the console."""
        rows, total_inv, total_val, total_gl, total_ret = self.get_portfolio_metrics()

        if not rows:
            print("\n[Info] Portfolio is currently empty.")
            return

        print("\n" + "=" * 100)
        print("                        INVESTMENT PORTFOLIO PERFORMANCE REPORT                          ")
        print("=" * 100)
        header = f"| {'Ticker':<6} | {'Shares':>7} | {'Buy Price':>10} | {'Curr Price':>10} | {'Invested ($)':>13} | {'Market Val ($)':>14} | {'Gain/Loss ($)':>14} | {'Return':>8} |"
        print(header)
        print("-" * 100)

        for r in rows:
            gl_indicator = "+" if r['GainLoss'] >= 0 else ""
            row_str = (
                f"| {r['Ticker']:<6} | {r['Shares']:>7} | ${r['BuyPrice']:>9.2f} | ${r['CurrentPrice']:>9.2f} | "
                f"${r['InvestedCapital']:>12.2f} | ${r['CurrentValue']:>13.2f} | "
                f"{gl_indicator}${r['GainLoss']:>12.2f} | {gl_indicator}{r['ReturnPct']:>6.2f}% |"
            )
            print(row_str)

        print("-" * 100)
        gl_sign = "+" if total_gl >= 0 else ""
        print(f" TOTAL INVESTED CAPITAL : ${total_inv:>14.2f}")
        print(f" CURRENT MARKET VALUE   : ${total_val:>14.2f}")
        print(f" TOTAL UNREALIZED P/L   : {gl_sign}${total_gl:>13.2f} ({gl_sign}{total_ret:.2f}%)")
        print("=" * 100)

    def export_to_csv(self):
        """Exports the active portfolio summary to an external CSV file."""
        rows, total_inv, total_val, total_gl, total_ret = self.get_portfolio_metrics()
        
        try:
            with open(self.output_file, mode="w", newline="", encoding="utf-8") as f:
                fieldnames = ["Ticker", "Shares", "BuyPrice", "CurrentPrice", "InvestedCapital", "CurrentValue", "GainLoss", "ReturnPct"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for r in rows:
                    writer.writerow({
                        "Ticker": r["Ticker"],
                        "Shares": r["Shares"],
                        "BuyPrice": f"{r['BuyPrice']:.2f}",
                        "CurrentPrice": f"{r['CurrentPrice']:.2f}",
                        "InvestedCapital": f"{r['InvestedCapital']:.2f}",
                        "CurrentValue": f"{r['CurrentValue']:.2f}",
                        "GainLoss": f"{r['GainLoss']:.2f}",
                        "ReturnPct": f"{r['ReturnPct']:.2f}%"
                    })
            print(f"\n[Export Success] Saved portfolio audit logs to '{self.output_file}'.")
            return True
        except Exception as e:
            print(f"[Error] Failed to export CSV: {e}")
            return False


def run_cli():
    tracker = PortfolioTracker()
    print("=================================================================")
    print("      DATHEON - STOCK PORTFOLIO PERFORMANCE TRACKER             ")
    print("=================================================================")

    while True:
        print("\n------------------- PORTFOLIO MENU -------------------")
        print("1. View Portfolio Performance Table")
        print("2. Add / Buy Stock Position")
        print("3. Remove / Sell Position")
        print("4. Update Current Market Price of a Ticker")
        print("5. Export Portfolio Summary to CSV")
        print("6. Exit")
        print("------------------------------------------------------")

        try:
            choice = input("Select an option (1-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting tracker.")
            break

        if choice == "1":
            tracker.display_portfolio()
        elif choice == "2":
            try:
                ticker = input("Enter Ticker Symbol (e.g. AAPL, GOOGL, MSFT): ")
                shares = int(input("Enter Number of Shares: "))
                price = float(input("Enter Purchase Price ($): "))
                tracker.add_position(ticker, shares, price)
            except ValueError as e:
                print(f"[Input Error] {e}")
        elif choice == "3":
            ticker = input("Enter Ticker to remove: ")
            tracker.remove_position(ticker)
        elif choice == "4":
            try:
                ticker = input("Enter Ticker Symbol: ").strip().upper()
                price = float(input(f"Enter New Current Market Price for {ticker} ($): "))
                tracker.market_prices[ticker] = price
                print(f"[Market Updated] {ticker} current price set to ${price:.2f}")
            except ValueError as e:
                print(f"[Input Error] {e}")
        elif choice == "5":
            tracker.export_to_csv()
        elif choice == "6":
            tracker.export_to_csv()
            print("\nPortfolio state saved. Happy Investing with Datheon!")
            break
        else:
            print("[Error] Invalid choice. Choose 1 to 6.")


if __name__ == "__main__":
    run_cli()
