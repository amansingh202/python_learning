#Monthly salary
income = float(input("Enter the monthly income"))

#Average debt
debt = float(input("Enter the average debt"))

#lower limit
lowLimit = 0.36*income - debt

#high limit
highLimit = 0.42*income - debt

print("Lower limit is: ",lowLimit)
print("Higher limit is: ",highLimit)