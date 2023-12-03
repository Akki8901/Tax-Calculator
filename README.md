# Tax-Calculator

Tax Calculator
Overview
The Tax Calculator is a simple command-line application written in Python. It calculates annual income tax based on user input, considering both federal and provinces taxes for Canada.

How to Run
Requirements:

Make sure you have Python installed on your system.
Clone the Repository:

bash
Copy code
git clone https://github.com/Akki_8901/tax-calculator.git
cd tax-calculator
Run the Program:

bash
Copy code
python tax_calculator.py
Follow the prompts to enter your annual income and province.

Sample Scenarios
Scenario 1: Standard Input
Enter your annual income: $60000
Enter your province: Ontario
Scenario 2: Invalid Province
Enter your annual income: $70000
Enter your province: Florida
Error: Invalid province entered.
Scenario 3: Invalid Income Input
Enter your annual income: Not a number
Error: Invalid input. Please enter a valid numerical value for income.
Code Structure
tax_calculator.py: Contains the main code for the Tax Calculator.

Classes:
TaxCalculator: Handles income tax calculations based on federal and provincial tax brackets.
TaxReport: Generates and prints a tax report.
Main Logic:
User input for income and province.
Validation of province input.
Tax calculation and report generation.
README.md: This file, providing instructions and insights.
