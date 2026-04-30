import csv
def stock_tracker():
    market_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 150.00,
        "AMZN": 175.00,
        "MSFT": 410.00
    }
    portfolio = []
    total_value = 0.0
    print("--- Stock Portfolio Tracker ---")
    print(f"Available Tickers: {', '.join(market_prices.keys())}\n")
    while True:
        ticker = input("Enter stock ticker (or type 'done' to calculate): ").upper() 
        if ticker == 'DONE':
            break
        if ticker not in market_prices:
            print(f"Error: {ticker} is not in our price database. Please try again.")
            continue
        try:
            quantity = float(input(f"Enter quantity of {ticker} owned: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numerical value for quantity.")
            continue
        price_per_share = market_prices[ticker]
        position_value = quantity * price_per_share
        total_value += position_value    
        portfolio.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price_per_share,
            "value": position_value
        })
    print("\n--- Portfolio Summary ---")
    print(f"{'Ticker':<10} | {'Quantity':<10} | {'Price':<10} | {'Value':<10}")
    print("-" * 45)   
    for item in portfolio:
        print(f"{item['ticker']:<10} | {item['quantity']:<10.2f} | ${item['price']:<9.2f} | ${item['value']:<10.2f}") 
    print("-" * 45)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")
    save_choice = input("\nWould you like to save this summary to a file? (y/n): ").lower()
    if save_choice == 'y':
        save_portfolio(portfolio, total_value)
def save_portfolio(portfolio, total_value):
    filename = "portfolio_summary.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ticker", "Quantity", "Price", "Position Value"])
            for item in portfolio:
                writer.writerow([item['ticker'], item['quantity'], item['price'], item['value']])
            writer.writerow([])
            writer.writerow(["TOTAL VALUE", "", "", f"${total_value:,.2f}"])
        print(f"Success! Portfolio saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving: {e}")
if __name__ == "__main__":
    stock_tracker()
