def how_many_months(initial_amount, rate):
    from numpy import log
    # Calculate duration required (Gives decimal value)
    minimum_duration = log(1000000/initial_amount)/log(1+rate/100)
    # Adds a 1 if minimum_value returns a decimal value
    months = int(minimum_duration) + int((minimum_duration - int(minimum_duration)) > 0)*(1)
    # Fix negative values that occurs when initial_amount greater than 1 mil
    if (months < 0):
        months = 0
    return months