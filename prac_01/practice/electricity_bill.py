# Calculate Electricity Bill
"""
get cents per kWh
get daily use in kWh
get days in billing period
total cost =
display total cost
"""
# TARIFF_11 = 0.244618
# TARIFF_31 = 0.136928

print("Electricity bill estimator")
cents_per_kwh = 35
daily_kwh = 4.5
number_of_days = 90
total_cost = number_of_days * (cents_per_kwh + daily_kwh)
print(f"${total_cost}")

"""
Expected output:

Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
"""
