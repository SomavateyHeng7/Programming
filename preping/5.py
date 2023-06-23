# Store the input values
start_month = int(input("Enter the starting month: "))
start_date = int(input("Enter the starting date: "))
working_days = int(input("Enter the total number of working days: "))

# Calculate the number of days in the starting month
days_in_month = 31
if start_month in [4, 6, 9, 11]:
    days_in_month = 30
elif start_month == 2:
    days_in_month = 28

# Initialize the deadline month and date
deadline_month = start_month
deadline_date = start_date + working_days

# Increment the deadline month if necessary
while deadline_date > days_in_month:
    deadline_month += 1
    deadline_date -= days_in_month
    if deadline_month > 12:
        deadline_month = 1
    days_in_month = 31
    if deadline_month in [4, 6, 9, 11]:
        days_in_month = 30
    elif deadline_month == 2:
        days_in_month = 28

# Print the deadline month and date
print("Deadline month:", deadline_month)
print("Deadline date:", deadline_date)