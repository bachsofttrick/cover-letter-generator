# Ask the user for the hourly rate
hourly_rate = float(input("Enter your hourly rate: "))

# Define the constants
hours_per_day = 8
days_per_week = 5
weeks_per_month = 4
months_per_year = 13

# Calculate annual salary
annual_salary = hourly_rate * hours_per_day * days_per_week * weeks_per_month * months_per_year

# Print the result
print(f"Your estimated annual salary is: ${annual_salary:.0f}")
