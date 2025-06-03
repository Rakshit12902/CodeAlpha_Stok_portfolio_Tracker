import csv
stock_prices = {
    "AAPL": 190.50,
    "GOOGL": 2800.75,
    "TSLA": 175.80,
    "AMZN": 3250.60,
    "MSFT": 410.30
}

def get_user_portfolio():
    portfolio = {}
    print("Enter your stock portfolio (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        total += price * quantity
    return total

def save_to_txt(portfolio, total):
    with open("portfolio_summary.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} x ${stock_prices[stock]:.2f}\n")
        f.write(f"\nTotal Investment: ${total:.2f}\n")
    print("Saved to portfolio_summary.txt")

def save_to_csv(portfolio, total):
    with open("portfolio_summary.csv", mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print("Saved to portfolio_summary.csv")

def main():
    portfolio = get_user_portfolio()
    total = calculate_total_investment(portfolio)
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} x ${stock_prices[stock]:.2f}")
    print(f"\nTotal Investment: ${total:.2f}")

    choice = input("Save results? (txt/csv/none): ").lower()
    if choice == "txt":
        save_to_txt(portfolio, total)
    elif choice == "csv":
        save_to_csv(portfolio, total)
    else:
        print("Results not saved.")

if __name__ == "__main__":
    main()
