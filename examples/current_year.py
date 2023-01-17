from jaldt import now

current_year_in_farsi = now(strftime='%y\n%Y')
current_year_in_fingi = now(strftime='%y\n%Y', lang='fingilish')

print(current_year_in_farsi)
print(current_year_in_fingi)