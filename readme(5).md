Description

This Python program analyzes resource request values entered by the user.
It categorizes them into different demand levels and applies a personalized filtering rule based on the user’s name.


How It Works
	1.	The user enters their full name.
	2.	Spaces are removed from the name.
	3.	The length of the name is calculated.
	4.	PLI (Personalized Logic Index) = Length % 3
	5.	The user enters the number of requests and the request values.
	6.	Requests are categorized into:
	•	Invalid Requests (less than 0)
	•	No Demand (0)
	•	Low Demand (1–20)
	•	Moderate Demand (21–50)
	•	High Demand (above 50)
	7.	Based on the PLI value, a rule is applied to remove certain categories.


PLI Rules
	•	PLI = 0 → Remove Low Demand
	•	PLI = 1 → Remove High Demand
	•	PLI = 2 → Remove Low, High, Invalid, and No Demand


Output

The program displays:
	•	Categories before filtering
	•	L value (length of name)
	•	PLI value
	•	Applied rule
	•	Total removed requests
	•	Categories after filtering
	•	Total valid requests


Requirements Followed
	•	Used lists
	•	Used for loops
	•	Used conditional statements
	•	Did not use list comprehension
	•	Did not use dictionaries or built-in functions like sum(), max(), min()

File
	•	day 5 challenges.py