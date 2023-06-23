import calendar
from datetime import datetime, timedelta

def get_deadline(start_month, start_date, total_days):
    # Convert the start month to a month number (1 for January, 2 for February, etc.)
    start_month_num = list(calendar.month_name).index(start_month)

    # Create a date object for the start date
    start_date = datetime(year=2022, month=start_month_num, day=start_date)

    # Calculate the deadline by adding the total number of working days to the start date
    deadline = start_date + timedelta(days=total_days)

    # Return the month and date of the deadline
    return calendar.month_name[deadline.month], deadline.day

# Test the function
start_month = 'January'
start_date = 1
total_days = 10
deadline_month, deadline_date = get_deadline(start_month, start_date, total_days)
print(f'The deadline is on {deadline_month} {deadline_date}')