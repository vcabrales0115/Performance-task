#Budget tracker

def savings(income, costs):
    return income - costs

income= input("What is your monthly income? ")
if income==ValueError:
    print("please enter a valid answer ")
monthly_costs = []


#running sequence of code using loops


while True:
    rent= int(input("How much is your rent this month? "))
    utillies= int(input("How much are your utillies this month? "))
    grocery= int(input("What is your average grocery costs per month? "))
    
    for cost in [rent, utillies, grocery]:
        if cost < 0:
            print("Please enter a valid answer")
    again= input("Enter again?(press q to quit, enter to repeat)")
    if again == "q":

        break
    else:
        continue
    #end loop


#Add costs together
#list including the costs of each catagory


monthly_costs = [rent, utillies, grocery]
total = rent + utillies + grocery
print(f"Your monthly costs are" ,total,"dollars")

#Subtract costs from income

balance_remaining= int(income)-total
print(f"You have a remaining balence of",balance_remaining,"dollars this month!")
