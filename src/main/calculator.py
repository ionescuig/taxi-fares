#!/usr/bin/env python
# description     :A calculator for the fare for a Hackney Carriage (Black Cab) in Plymouth, UK
# author          :Gabriel Ionescu
# date            :2018/12/04
# ==============================================================================

"""
A calculator for the fare for a Hackney Carriage (Black Cab) in Plymouth, UK.
The fare is not fixed, is affected by the traffic and tolls (ex: for Cornwall).
"""


def check_tariff(date, hour, bank_holiday):
    """
    Check the tariff for a date and time.
    """

    WEEKDAY = date.strftime('%A')
    MONTH = date.strftime('%m')
    DAY = date.strftime('%d')
    TIME_HOUR = int(hour.strftime('%H'))
    tariff = ''

    # calculate the right tariff
    if bank_holiday is True or WEEKDAY == 'Sunday':
        if TIME_HOUR > 19:
            tariff = 'Three'
        elif TIME_HOUR > 6:
            tariff = 'Two'
        else:
            tariff = 'Three'
    elif TIME_HOUR > 19:
        tariff = 'Two'
    elif TIME_HOUR > 6:
        tariff = 'One'
    else:
        tariff = 'Three'

    if MONTH == '12':
        if DAY == '24':
            if TIME_HOUR > 19:
                tariff = 'Four'
        elif DAY == '25':
            if TIME_HOUR < 7:
                tariff = 'Four'
            else:
                tariff = 'Five'
        elif DAY == '26':
            if TIME_HOUR < 7:
                tariff = 'Five'
            else:
                tariff = 'Four'
        elif DAY == '27':
            if TIME_HOUR < 7:
                tariff = 'Four'
        elif DAY == '31':
            if TIME_HOUR > 19:
                tariff = 'Four'
    elif MONTH == '01':
        if DAY == '01':
            if TIME_HOUR < 7:
                tariff = 'Five'
            else:
                tariff = 'Four'
        elif DAY == '02':
            if TIME_HOUR < 7:
                tariff = 'Four'

    return tariff


def calculate_fare(tariff, miles, no_of_people, toll):
    # calculate the fare
    if miles < 0.1:
        fare = tariff[0]
    elif miles == 0.1:
        fare = tariff[0] + tariff[1]
    else:
        multiplier = (miles - 0.2) // 0.2

        if miles < 5:
            waiting = miles
        else:
            waiting = 5
        waiting_time = ((waiting * tariff[3]) // tariff[3]) * tariff[3]

        fare = tariff[0] + tariff[1] + tariff[2] * multiplier + waiting_time
    if no_of_people > 2:
        fare += (no_of_people - 2) * 0.2
    if toll:
        fare += toll
        
    return fare
