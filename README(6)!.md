# 📊 Transaction Risk Analyzer

## 📌 Overview

The **Transaction Risk Analyzer** is a Python program designed to monitor and evaluate daily financial transactions. It categorizes transactions, detects unusual spending patterns, and generates a risk report to help identify potential fraud or abnormal activity.

This project demonstrates how programming concepts can be applied to **real-world financial monitoring systems**.

---

## ⚙️ Features

* Accepts user input for multiple transactions
* Handles edge cases (e.g., no transactions entered)
* Classifies transactions into:

  * Normal (1–500)
  * Large (501–2000)
  * High Risk (>2000)
  * Invalid (≤0)
* Uses **list comprehension** to filter valid transactions
* Calculates:

  * Total transaction value
  * Average spending (valid transactions only)
  * Number of transactions
* Detects patterns:

  * Frequent transactions (>5)
  * Large total spending (>5000)
  * Suspicious high-risk activity (≥3 transactions)
* Displays a formatted **risk report**
* Provides a **security alert** for invalid transactions

---

## 🧠 Logic & Approach

### 1. Input Handling

* User enters the number of transactions.
* If no transactions are entered, the program exits safely.

### 2. Transaction Classification

* Each transaction is evaluated and categorized using conditional statements.
* Data is stored in a dictionary for structured organization.

### 3. Data Processing

* Valid transactions are filtered using **list comprehension**.
* Total value and average spend are calculated using built-in functions.

### 4. Pattern Detection

* Frequent Transactions → more than 5 transactions
* Large Spending → total exceeds 5000
* Suspicious Pattern → 3 or more high-risk transactions

### 5. Risk Evaluation

* High Risk → suspicious activity detected
* Moderate Risk → frequent or large spending
* Low Risk → otherwise

---

## 📊 Output

The program generates a detailed report including:

* Categorized transactions
* Total transaction value
* Average valid spending
* Number of transactions
* Final risk classification
* Alerts for invalid transactions

---

## 🛠️ Technologies Used

* Python
* Core concepts:

  * Lists
  * Loops (`for`)
  * Conditional statements
  * Dictionary
  * Tuple
  * List comprehension
  * Built-in functions (`sum()`, `len()`)

---

## ▶️ How to Run

1. Run the Python script
2. Enter the number of transactions
3. Input each transaction amount
4. View the generated transaction risk report

---

## 🎯 Learning Outcomes

* Handling user input and edge cases
* Efficient use of data structures (lists, dictionaries)
* Applying conditional logic for classification
* Using list comprehension for data filtering
* Implementing simple risk analysis techniques

---

## 🔐 Security Insight

The program identifies invalid or negative transactions and raises a **security alert**, simulating a basic fraud detection mechanism.

---

## 🏁 Conclusion

This project simulates a simple yet effective **transaction monitoring system**. It highlights how structured programming can help detect risky financial behavior and improve decision-making.

---

## 👤 Author

Student Project Submission
