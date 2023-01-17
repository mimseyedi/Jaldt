from jaldt import now

current_weekday_in_farsi = now(strftime='%a\n%A')
current_weekday_in_fingi = now(strftime='%a\n%A', lang='fingilish')

print(current_weekday_in_farsi)
print(current_weekday_in_fingi)