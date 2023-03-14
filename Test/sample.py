from datetime import datetime

input_datetime_str = '18,September 2023'
input_datetime_obj = datetime.strptime(input_datetime_str, '%d,%B %Y')

if input_datetime_obj < datetime.today():
    print('The input date is in the past. Please enter valid date.')
