#!/usr/bin/env python
# description     :A calculator for the fare for a Hackney Carriage (Black Cab) in Plymouth, UK
# author          :Gabriel Ionescu
# date            :2018/12/04
# ==============================================================================

"""
A calculator for the fare for a Hackney Carriage (Black Cab) in Plymouth, UK.
The fare is not fixed, is affected by the traffic and tolls (ex: for Cornwall),
for 1-2 people (each extra passenger after the second passenger: 20p).
"""

import datetime
from time import strftime


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
            tariff = 'three'
        elif TIME_HOUR > 6:
            tariff = 'two'
        else:
            tariff = 'three'
    elif TIME_HOUR > 19:
        tariff = 'two'
    elif TIME_HOUR > 6:
        tariff = 'one'
    else:
        tariff = 'three'

    if MONTH == '12':
        if DAY == '24':
            if TIME_HOUR > 19:
                tariff = 'four'
        elif DAY == '25':
            if TIME_HOUR < 7:
                tariff = 'four'
            else:
                tariff = 'five'
        elif DAY == '26':
            if TIME_HOUR < 7:
                tariff = 'five'
            else:
                tariff = 'four'
        elif DAY == '27':
            if TIME_HOUR < 7:
                tariff = 'four'
        elif DAY == '31':
            if TIME_HOUR > 19:
                tariff = 'four'
    elif MONTH == '01':
        if DAY == '01':
            if TIME_HOUR < 7:
                tariff = 'five'
            else:
                tariff = 'four'
        elif DAY == '02':
            if TIME_HOUR < 7:
                tariff = 'four'

    return tariff


def calculate_tariff(tariff_fare, miles, no_of_people, toll):
    # calculate the fare
    if miles < 0.1:
        fare = tariff_choice[0]
    elif miles == 0.1:
        fare = tariff_choice[0] + tariff_choice[1]
    else:
        multiplier = (miles - 0.2) // 0.2

        if miles < 5:
            waiting = miles
        else:
            waiting = 5
        waiting_time = ((waiting * tariff_choice[3]) // tariff_choice[3]) * tariff_choice[3]

        fare = tariff_choice[0] + tariff_choice[1] + tariff_choice[2] * multiplier + waiting_time
    if no_of_people > 2:
        fare += (no_of_people - 2) * 0.2
    if toll:
        fare += toll
        
    # print('tariff: ', tariff_choice)
    print('Fare: %.2f' % fare)


if __name__ == "__main__":
    """
    as a standalone:
    calculates the fare for this hour, for a selected number of miles
    """
    no_of_miles = float(input("Miles: "))
    no_of_people = input("Number of people: ")
    if no_of_people:
        no_of_people = int(no_of_people)
    else:
        no_of_people = 1
    toll = input("Toll: ")
    if toll:
        toll = float(toll)
    else:
        toll = 0
    test_tariff = check_tariff(datetime.datetime(2019, 5, 6, 2, 51, 5),
                               datetime.datetime(2019, 5, 6, 2, 51, 5),
                               bank_holiday=True)
    print(test_tariff)
    input("\nPress any key to exit...")
