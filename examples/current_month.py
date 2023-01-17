from jaldt import now

current_month_in_farsi = now(strftime='%B\n%b\n%m')
current_month_in_fingi = now(strftime='%B\n%b\n%m', lang='fingilish')

print(current_month_in_farsi)
print(current_month_in_fingi)