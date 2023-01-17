from jaldt import events

dey_events = events(month='dey')

try:
    user_input = input("Please enter a date with farsi numbers: ")
    print(dey_events[user_input])

except KeyError:
    print("There are no events for this date!")