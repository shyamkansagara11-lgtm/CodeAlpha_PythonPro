# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

total_investment = 0

# Step 2: Take input
n = int(input("How many stocks you want to enter: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Step 3: Calculate investment
    if stock_name in stock_prices:
        value = stock_prices[stock_name] * quantity
        total_investment += value
        print("Added:", stock_name, "Value =", value)
    else:
        print("Stock not found!")

# Step 4: Show result
print("\nTotal Investment Value =", total_investment)

# Step 5: Save to file (optional)
with open("investment.txt", "w") as file:
    file.write("Total Investment = " + str(total_investment))

print("Data saved in investment.txt")