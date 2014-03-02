"""
    Problem 19
    Counting Sundays
        Counts all Sundays that land on the first of a month
        between the years 1901 and 2000
"""
def get_month_days(leap=False):
    month_days = { 1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,
            11:30, 12:31 }
    if(leap):
        month_days[2] = 29
    return month_days

def is_leap_year( year ):
    is_leap = False
    if year % 4 == 0:
            is_leap = ( year % 100 != 0 or year % 400 == 0 )
    return is_leap

def count_sundays_first_month(start_day, year_start, year_end):
    month_days = get_month_days()
    month_days_leap = get_month_days(True)
    sundays = 0

    for year in range(year_start, year_end + 1):
        is_leap = is_leap_year
        days_month_map = month_days if not is_leap else month_days_leap

        for month in days_month_map:
            if start_day == 0:
                sundays += 1
            days = days_month_map[month]
            day_offset = days % 7
            start_day = ( start_day + day_offset ) % 7

    return sundays

if __name__ == '__main__':
    print count_sundays_first_month(2, 1901, 2000)
