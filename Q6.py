def print_calendar(start_day, days_in_month):
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    print(" ".join(week_days))
    
    start_day_index = week_days.index(start_day)
    print("    " * start_day_index, end="")
    
    current_day = 1
    
    while current_day <= days_in_month:
        print(f"{current_day: > 4}", end="")
        start_day_index += 1
     
        if start_day_index % 7 == 0:
            print()
        
        current_day += 1

start_day = "Wed"
days_in_month = 31

print_calendar(start_day, days_in_month)
