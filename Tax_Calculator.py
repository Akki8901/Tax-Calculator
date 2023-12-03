class TaxCalculator:
    
    def __init__(self, income, province):
        
        self.income = income
        self.province = province

    # Simplified federal tax calculation logic for Canada
    def calculate_federal_tax(self):
        
        federal_brackets = [(0, 10000), (10001, 50000), (50001, 100000)]
        federal_rates = [0.15, 0.20, 0.25]

        return self._calculate_tax(self.income, federal_brackets, federal_rates)

    # Simplified provincial tax calculation logic for Canada provinces
    def calculate_province_tax(self):

        province_brackets = {
            "Alberta": [(0, 15000), (15001, 75000), (75001, 100000)],
            "British Columbia": [(0, 20000), (20001, 80000), (80001, 100000)],
            "Manitoba": [(0, 18000), (18001, 75000), (75001, 100000)],
            "New Brunswick": [(0, 16000), (16001, 70000), (70001, 100000)],
            "Newfoundland and Labrador": [(0, 17000), (17001, 80000), (80001, 100000)],
            "Northwest Territories": [(0, 20000), (20001, 90000), (90001, 100000)],
            "Nova Scotia": [(0, 19000), (19001, 85000), (85001, 100000)],
            "Nunavut": [(0, 18000), (18001, 80000), (80001, 100000)],
            "Ontario": [(0, 22000), (22001, 90000), (90001, 100000)],
            "Prince Edward Island": [(0, 17000), (17001, 75000), (75001, 100000)],
            "Quebec": [(0, 18000), (18001, 85000), (85001, 100000)],
            "Saskatchewan": [(0, 16000), (16001, 70000), (70001, 100000)],
            "Yukon": [(0, 15000), (15001, 80000), (80001, 100000)],
        }

        province_rates = [0.10, 0.15, 0.20]

        return self._calculate_tax(self.income, province_brackets[self.province], province_rates)

    # Method to calculate tax based on provided brackets and rates
    def _calculate_tax(self, income, brackets, rates):
        tax = 0
        for i in range(len(brackets)):
            if income > brackets[i][1]:
                tax += (brackets[i][1] - brackets[i][0] + 1) * rates[i]
            else:
                tax += (income - brackets[i][0] + 1) * rates[i]
                break
        return tax

class TaxReport:
    def __init__(self, income, federal_tax, province_tax):
        self.income = income
        self.federal_tax = federal_tax
        self.province_tax = province_tax

    # Method to generate and print a tax report
    def generate_report(self):
        print("\n","-"*75)
        print("\t\tHere is your Tax Report:")
        print("-"*75)
        print(f"Annual Income: ${self.income}")
        print(f"Federal Income Tax: ${self.federal_tax}")
        print(f"{user.province} Income Tax: ${self.province_tax}")
        print(f"Total Tax: ${self.federal_tax + self.province_tax}")

# Sample usage in a command-line interface
if __name__ == "__main__":
    print("\n","*" *75)
    print("\t\t\t TAX CALCULATOR ")
    print("*" *75)
    try:
        # Get user input for income and province
        income = float(input("\nEnter your annual income: $"))
        province = input("Enter your province: ")

        # Validate the entered province
        if province not in [
            "Alberta", "British Columbia", "Manitoba", "New Brunswick",
            "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia",
            "Nunavut", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"
        ]:
            raise ValueError("Invalid province entered.")

        # Create a TaxCalculator instance
        user = TaxCalculator(income, province)
        
        # Calculate federal and provincial taxes
        federal_tax = user.calculate_federal_tax()
        province_tax = user.calculate_province_tax()

        # Generate and print a tax report
        report = TaxReport(income, federal_tax, province_tax)
        report.generate_report()

# Handle ValueError (e.g., invalid input for income or province)
    except ValueError as e:
        print(f"Error: {e}")
        
# Handle other unexpected exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
