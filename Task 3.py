def get_date_in_format(date):
    dates = date.split('.')
    return f"{dates[2]}.{dates[1]}.{dates[0]}"
