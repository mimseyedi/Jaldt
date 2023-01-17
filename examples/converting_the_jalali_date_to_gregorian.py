from jaldt import j2g

j_year, j_month, j_day = 1401, 7, 20

g_year, g_month, g_day = j2g(j_year, j_month, j_day)

print(f'{g_year}/{g_month}/{g_day}')