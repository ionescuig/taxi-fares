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

from time import strftime


def check_tariff(date, hour, bank_holiday):
    """
    Check the tariff for a date and time.
    """

    tariff_choice = ''

    # calculate the right tariff
    if bank_holiday or date.strftime('%A') == 'Sunday':
        if 6 <= int(hour.strftime('%H')) < 19:
            tariff_choice = 'tariff_2'
        elif int(hour.strftime('%H')) >= 19:
            tariff_choice = 'tariff_3'
    elif date.strftime('%m') == '01':
        if date.strftime('%d') == '01':
            if int(hour.strftime('%H')) < 7:
                tariff_choice = 'tariff_5'
            else:
                tariff_choice = 'tariff_4'
        elif date.strftime('%d') == '02':
            if int(hour.strftime('%H')) < 7:
                tariff_choice = 'tariff_4'
    elif date.strftime('%m') == '12':
        if date.strftime('%d') == '24' and int(hour.strftime('%H')) > 19:
            tariff_choice = 'tariff_4'
        elif date.strftime('%d') == '25':
            if int(hour.strftime('%H')) < 7:
                tariff_choice = 'tariff_4'
            else:
                tariff_choice = 'tariff_5'
        elif date.strftime('%d') == '26':
            if int(hour.strftime('%H')) < 7:
                tariff_choice = 'tariff_5'
            else:
                tariff_choice = 'tariff_4'
        elif date.strftime('%d') == '27':
            if int(hour.strftime('%H')) < 7:
                tariff_choice = 'tariff_4'
        elif date.strftime('%d') == '31' and 19 <= int(hour.strftime('%H')):
            tariff_choice = 'tariff_4'
    elif 6 <= int(hour.strftime('%H')) < 19:
        tariff_choice = 'tariff_1'
    elif int(hour.strftime('%H')) >= 19:
        tariff_choice = 'tariff_2'
    else:
        tariff_choice = 'tariff_3'

    return tariff_choice


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
    calculate(strftime, no_of_miles, no_of_people, toll)
    input("\nPress any key to exit...")
