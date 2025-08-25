# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 140,
    "MSFT": 330
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# User input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("Stock not found. Try again.")

# Calculate total
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

print(f"\nTotal Investment Value: ${total_value}")

# Save results to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio saved in 'portfolio_summary.txt'")
