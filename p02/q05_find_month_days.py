year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
months_with_30_days = [4,6,9,11]
months_with_31_days = [1,3,5,7,8,10,12]

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month == 2:
    print("Month 2 in year {0} has 29 days".format(year))
elif month == 2:
    print("Month 2 in year {0} has 28 days".format(year))
elif month in months_with_30_days:
    print("Month {0} in year {1} has 30 days".format(month,year))
elif month in months_with_31_days:
    print("Month {0} in year {1} has 31 days".format(month,year))
