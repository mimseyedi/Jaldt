from jaldt import now

digital_clock_in_farsi = now(strftime='%I:%M %p')
digital_clock_in_fingi = now(strftime='%I:%M %p', lang='fingilish')

print(digital_clock_in_farsi)
print(digital_clock_in_fingi)