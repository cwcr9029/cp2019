name = input("Enter name: ")
weekly_hours = int(input("Enter number of hours worked weekly: "))
hourly_pay = float(input("Enter hourly pay rate: "))
cpf_contribution_rate = float(input("Enter CPF contribution rate(%): "))
gross_pay = weekly_hours * hourly_pay
cpf_contribution = gross_pay * (cpf_contribution_rate / 100)
net_pay = gross_pay - cpf_contribution

print("Payroll statement for " + name)
print("Number of hours worked in week: " + str(weekly_hours))
print("Hourly pay rate: $" + str(hourly_pay))
print("Gross pay = ${0:.2f}".format(gross_pay))
print("CPF contribution at 20% = ${0:.2f}".format(cpf_contribution))
print("Net pay = ${0:.2f}".format(net_pay))