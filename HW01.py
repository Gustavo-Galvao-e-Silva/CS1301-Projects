"""
Georgia Institute of Technology - CS1301
Homework 1 - Functions & Expressions
"""

#########################################

# Program Constants:
ROUNDING_PRECISION = 2

"""
Function Name: weekOfWelcome()
Parameters: N/A
Returns: None (NoneType)
"""

def weekOfWelcome():
    event_day_of_week = input("Enter the day of the week: ")
    event_time = input("Enter the time of the event: ")
    event_location = input("Enter the location of the event: ")
    event_club_name = input("Enter the name of the club hosting the event: ")

    print(f"{event_day_of_week}, {event_time}, {event_location}: WoW event by the {event_club_name} Club.")

#########################################

"""
Function Name: ramblinReck()
Parameters: N/A
Returns: None (NoneType)
"""



def ramblinReck():
    P = 10_000
    PI = 3.14

    reck_distance = int(input("How far away are you from the Reck? "))

    ramblin_intensity = P / (4 * PI * (reck_distance ** 2))
    print(f"The Ramblin' Reck is {round(ramblin_intensity, ROUNDING_PRECISION)} Watts loud!")

#########################################

"""
Function Name: diningDollars()
Parameters: N/A
Returns: None (NoneTyoe)
"""

def diningDollars():
    item_cost_dict = {
        "drink": 3,
        "appetizer": 6,
        "main course": 11,
        "dessert": 3
    }

    TIP_PERCENTAGE = 0.2
    INITIAL_DINING_DOLLARS = 23.0

    meal_cost = 0

    for item, cost in item_cost_dict.items():
        item_quantity = int(input(f"How many {item}s are you having? "))
        meal_cost += item_quantity * cost
    
    total_cost_with_tip = (1 + TIP_PERCENTAGE) * meal_cost
    dining_dollars_in_account = INITIAL_DINING_DOLLARS - total_cost_with_tip

    print(f"You have spent a total of {round(total_cost_with_tip, ROUNDING_PRECISION)} dining dollars and have {round(dining_dollars_in_account, ROUNDING_PRECISION)} dining dollars left!")

#########################################

"""
Function Name: findTs()
Parameters: N/A
Returns: None(NoneType)
"""

def findTs():
    number_of_places = int(input("How many locations do we need to search on campus? "))
    number_of_people_searching = int(input("How many people do we plan on searching with? "))

    number_of_ts_total = number_of_places ** 2
    minutes_per_single_t = number_of_people_searching / 2

    total_minutes_to_find_ts = number_of_ts_total * minutes_per_single_t

    hours_to_find_ts = int(total_minutes_to_find_ts // 60)
    minutes_remaining_to_find_ts = total_minutes_to_find_ts % 60

    print(f"It will take {hours_to_find_ts} hour(s) and {round(minutes_remaining_to_find_ts, ROUNDING_PRECISION)} minute(s) to find all of the T's!")

findTs()

#########################################

"""
Function Name: leftOverTime()
Parameters: N/A
Returns: None (NoneType)
"""

def leftOverTime():
    TOTAL_WEEK_HOURS = 168

    credit_hours = int(input("How many credit hours are you taking? "))
    education_time_per_week = 4 * credit_hours

    sleep_hours_per_night = float(input("How much sleep do you want to get each night? "))
    sleep_time_per_week = 7 * sleep_hours_per_night

    number_of_extracurriculars = int(input("How many extracurriculars do you participate in? "))
    extracuricular_time_per_week = 4 * number_of_extracurriculars

    free_time_activity = input("What activity do you want to do in your free time? ")

    occupied_time = education_time_per_week + sleep_time_per_week + extracuricular_time_per_week
    remaining_free_time = TOTAL_WEEK_HOURS - occupied_time

    print(f"You have {remaining_free_time} hours this week to do {free_time_activity}.")
    


#########################################
