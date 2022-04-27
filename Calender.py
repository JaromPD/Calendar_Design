def is_leap_year(year):
    """poo
    Finds out if a given year is a leap year.
    Returns a boolean.
    """

    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def days_in_month(month, year):
    """
    Finds the number of days that the given month has in the given year.
    Returns an integer of those days.
    """

    # If the month is February, the amount of days could change 
    # if the given year is a leap year
    if month == 2:
        if is_leap_year(year) == True:
            return 29
        else:
            return 28
    # These months have 31 days.
    elif month in [1, 3, 5, 7 , 8, 10, 12]:
        return 31
    # These have 30.
    elif month in [4, 6 , 9, 11]:
        return 30

def days_between(user_month, user_year):
    """
    Finds the number of days between the starting date of 1/1/1753 and the given month and year.
    Returns an integer of those days.
    """

    days_between = 0
    years_between = user_year - 1753
    total_days = 0

    # For every year we need to go through and add the days for
    # every month in that year.
    for year in range(0, years_between + 1):
        # If the year is the last year to loop through 
        # the program only needs to add up days until the month given
        for month in range(1, user_month if year == years_between else 13):
            total_days += days_in_month(month, 1753 + year)
    
    return(total_days)


def first_day_of_month(days_between):
    """
    Finds out what day of the week the first day of the given month will be
    using a starting day of 1/1/1753 which was Monday. This function returns
    an integer corresponding with the day of week. IE 2 = Monday.
    """

    # The starting day is Monday.
    day_of_week = 2

    # The loop goes through everyday between the starting Monday and the user's year and month.
    for day in range(1, days_between + 1):
        # If the day of the week is less than Saturday...
        if day_of_week < 7:
            # One more day of week is added.
            day_of_week += 1
        # If it is Saturday...
        else:
            # The day of week restarts on Monday.
            day_of_week = 1

    return(day_of_week)

def display_calendar(first_day, number_of_days):
    """
    This function displays the data as a readable calendar.
    """

    # The date starts at 0.
    date = 0

    print(" Su  Mo  Tu  We  Th  Fr  Sa ")
    # The blank days are printed at the beginning of the calendar.
    for blank_day in range(1, first_day):
        print("    ", end ="")

    # The date loop starts after the blank days, and goes until the last number of day.
    for day in range(blank_day, number_of_days + blank_day):
        # Date is the number that displays. It increases by 1 every loop.
        date += 1
        # if the day we're on (not date) is divisible by 7, a new line is started.
        if day % 7 == 0:
            print(f"")
        # If the date is less than 10 it will only take up 1 space, so it needs an extra space to
        # keep everything lined up.
        if date < 10:
            print(f"  {date} ", end ="")
        # The end = "" is to make sure Python doesn't automatically print a new line.
        else:
            print(f" {date} ", end ="")

def main():
    """
    This is the starting point, and runs all the functions in order to make a cohesive program.
    """
    valid_month_response = False
    valid_year_response = False

    while valid_month_response == False:
            try:
                month = int(input("Enter a month number: "))
                valid_month_response = True
            except ValueError:
                print("ERROR: Must be an integer.")
        
    while valid_year_response == False:
            try:
                year = int(input("Enter a year: "))
                valid_year_response = True
            except ValueError:
                print("ERROR: Must be an integer.")

    first_day = first_day_of_month(days_between(month, year))
    display_calendar(first_day, days_in_month(month, year))

# This runs the main function.
if __name__ == "__main__":
    main()

