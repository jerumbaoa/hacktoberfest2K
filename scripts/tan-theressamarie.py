# Calculates expiry date and expiry remaning days
import datetime

def calculate_expiry(date_joined, duration):

    date_joined = datetime.datetime.strptime(date_joined, '%Y-%m-%d')

    expiry_date = date_joined + datetime.timedelta(duration)

    print('Your time to hack will end on {}.'.format(expiry_date.date()))

    expiry_days = (expiry_date.date() - datetime.datetime.today().date()).days

    print('You still have {} days to HACK \m/'.format(expiry_days))

calculate_expiry('2019-10-01', 30)