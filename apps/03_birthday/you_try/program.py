import datetime


def print_header():
    print('-----------------------')
    print('BIRTHDAY CALCULATOR APP')
    print('-----------------------')
    print()


def get_birthday_from_user():
    print("When were you born")
    year = int(input("Year: "))
    month = int(input ("month: "))
    day = int(input("day: "))

    return datetime.date(year, month, day)


def compute_days_between_dates(original_date, target_date):
    current_year = datetime.date(target_date.year, original_date.month, original_date.day)
    days = current_year - target_date
    return days.days


def print_birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago".format(-days))
    elif days > 0:
        print("Your birthday is {} days from now".format(days))
    else:
        print("Happy Birthday!")


def main():
    print_header()
    birthday = get_birthday_from_user()
    current_date = datetime.date.today()
    number_of_days = compute_days_between_dates(current_date, birthday)
    print_birthday_information(number_of_days)


main()
