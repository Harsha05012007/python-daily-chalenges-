n = int(input("enter number of transactions :"))
if n <= 0:
    print("No transactions to process today. Goodbye!")
    exit()
transactions = []

for i in range(n):
    transactions.append(int(input("enter amount :")))

categorized = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

for t in transactions:
    if t <= 0:
        categorized["invalid"].append(t)
    elif 1 <= t <= 500:
        categorized["normal"].append(t)
    elif 501 <= t <= 2000:
        categorized["large"].append(t)
    else:
        categorized["high_risk"].append(t)

valid_transactions = [t for t in transactions if t > 0]

total_value = sum(valid_transactions)
num_transactions = len(transactions)
if len(valid_transactions) > 0:
    average_spend = total_value / len(valid_transactions)
else:
    average_spend = 0

frequent_transactions = num_transactions > 5
large_spending = total_value > 5000
suspicious_pattern = len(categorized["high_risk"]) >= 3
if frequent_transactions:
    print(f"Frequent Transactions: {frequent_transactions}")
if suspicious_pattern:
    print(f"Suspicious Transactions: {suspicious_pattern}")
if large_spending:
    print(f"Large Transactions: {large_spending}")

if suspicious_pattern:
    risk = "High Risk"
elif large_spending or frequent_transactions:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

summary = (total_value, num_transactions, risk)

print(".....Transaction Risk Report.....")
print(f"Categorized Transactions: {categorized}")
print(f"Total Transaction Value: ${summary[0]}")
print(f"Average Valid Spend: ${average_spend:.2f}")
print(f"Number of Transactions: {summary[1]}")
print(f"Risk Classification: {summary[2]}")
print("." * 31)
if len(categorized["invalid"]) > 0:
    print(f"\n SECURITY ALERT: {len(categorized['invalid'])} invalid/negative transaction attempted.")