from jaldt import events

current_month_events = events()

for day, event in current_month_events.items():
    print(day, event)