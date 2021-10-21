def convert_hours(total_hours):
total_hours=7
days=total_hours//24
weeks=days//7
return weeks,days,hours
print(convert_hours(7))