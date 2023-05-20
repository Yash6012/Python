# Historical data as a list of tuples
historical_data = [(10000, 0.08, 0.04), (12000, 0.06, 0.05), (15000, 0.1, 0.03)]

# Year for which you want to calculate real returns and change in purchasing power
year = 2023

# Loop through each year's data
for i, data in enumerate(historical_data):
    # Unpack the tuple
    initial_investment, nominal_return, inflation_rate = data

    # Calculate the real return and change in purchasing power
    real_return = (1 + nominal_return) / (1 + inflation_rate) - 1
    real_return_percent = real_return * 100
    change_in_purchasing_power = initial_investment * (1 + real_return) ** (year - 2022)

    # Output the results
    print(f"Year {year + i}:")
    print(f"Real Return: {real_return_percent:.2f}%")
    print(f"Change in Purchasing Power: Rs. {change_in_purchasing_power:.2f}\n")