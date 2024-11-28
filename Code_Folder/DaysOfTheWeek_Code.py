# Adding variables to store the inputs of the beginning week day of the holidays and its duration
day_week = str(input("Please state the day of the week in which your holidays start: "))
length_stay = int(input("How many days will be your holidays?: "))

# Here we are adding a simple list with the correct order of the week days, so we can use its index for the math part of the code
days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def endHolidays(day, length):
    # Itenarating over the list elements to find a match to a day of the week or find out that the input is not one
    for days in days_of_week:
        if days == day.strip().lower():
            dex = days_of_week.index(days)
            break
        else:
            return "That's not a valid day of the week."

    end = (dex + length) % 7
    return "You will return from your holidays on a {}.".format(days_of_week[end])

print(endHolidays(day_week, length_stay))
