from datetime import datetime

def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    date1 = datetime.strptime(date1, date_format)
    date2 = datetime.strptime(date2, date_format)
    delta = date2 - date1
    return delta.days
