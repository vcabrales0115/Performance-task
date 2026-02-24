#Budget tracker
def savings(income, costs):
    return income - costs

income= input("What is your monthly income? ")
if income==ValueError:
    print("please enter a valid answer ")
monthly_costs = []
while True:
    rent= int(input("How much is your rent this month? "))
    utillies= int(input("How much are your utillies this month? "))
    grocery= int(input("What is your average grocery costs per month? "))
    
for cost in [rent, utillies, grocery]:
    if cost < 0:
        print("Please enter a valid answer")
        break   
    

#Add costs together
total = rent + utillies + grocery
monthly_costs= rent + utillies + grocery
print(f"Your monthly costs is", {total})
if monthly_costs >0:
    def subtract(income, monthly_costs):
        discretionary_income = income - monthly_costs
        print(discretionary_income)
else:
    print("Try again")

# #Subtract costs from income
# def subtract (income, monthly_costs):
#     discretionary_income = income - monthly_costs
#     discretionary_income





# Updated_list = {rent, utillies*, miscellaneous**}
# print(Updated_list(rent, utillies, miscellaneous))