employee_name =  input("Enter your employee name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_per_hour = float(input("Enter your pay per hour: "))
gross_salary = hours_worked * pay_per_hour
tax = gross_salary * 0.1
net_salary = gross_salary - tax

print("------------SALARY REPORT-----------")
print(f"Employee Name: {employee_name}")
print(f"Hours Worked: {hours_worked}")
print(f"Pay per Hour: {pay_per_hour} dollars")
print(f"Gross Salary: {gross_salary:.2f} dollars")
print(f"Tax: {tax:.2f} dollars")
print(f"Net Salary: {net_salary:.2f} dollars")
print("------------------------------")
