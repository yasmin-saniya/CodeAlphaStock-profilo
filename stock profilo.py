stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"Added {quantity} shares of {stock} (${stock_prices[stock]} each) = ${investment}\n")

# Display result
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("Would you like to save this to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (without extension): ")
    with open(filename + ".txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to {filename}.txt")

