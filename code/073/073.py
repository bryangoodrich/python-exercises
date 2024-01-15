import calendar

print(calendar.calendar(2023))  
#                                  2023
#
#       January                         March
# Mo Tu We Th Fr Sa Su            Mo Tu We Th Fr Sa Su
#                    1                   1  2  3  4  5
#  2  3  4  5  6  7  8             6  7  8  9 10 11 12
#  9 10 11 12 13 14 15    ...     13 14 15 16 17 18 19
# 16 17 18 19 20 21 22            20 21 22 23 24 25 26
# 23 24 25 26 27 28 29            27 28               
# 30 31
#
#                         ...
#
#       October                         December
# Mo Tu We Th Fr Sa Su            Mo Tu We Th Fr Sa Su
#                    1                         1  2  3
#  2  3  4  5  6  7  8             4  5  6  7  8  9 10
#  9 10 11 12 13 14 15    ...     11 12 13 14 15 16 17
# 16 17 18 19 20 21 22            18 19 20 21 22 23 24
# 23 24 25 26 27 28 29            25 26 27 28 29 30 31
# 30 31


print(calendar.month(2023, 4))
#      April 2023
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

print(calendar.day_abbr[:])
# ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(calendar.month_name[:])
# ['', 'January', 'February', 'March', ...

aday = calendar.weekday(2023, 12, 25)
print(calendar.day_name[aday])
# Monday