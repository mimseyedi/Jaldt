from jaldt import g2j

g_year, g_month, g_day = 2022, 10, 12

j_year, j_month, j_day = g2j(g_year, g_month, g_day)

print(f'{j_year}/{j_month}/{j_day}')