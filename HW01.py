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
# weekOfWelcome helper functions:
def _print_formatted_week_of_welcome(event_day_of_week: str, event_time: str, event_location: str, event_club_name: str) -> None:
    print(f"{event_day_of_week}, {event_time}, {event_location}: WoW event by the {event_club_name} Club.")


# weekOfWelcome main function:
def weekOfWelcome() -> None:
    event_day_of_week = input("Enter the day of the week: ")
    event_time = input("Enter the time of the event: ")
    event_location = input("Enter the location of the event: ")
    event_club_name = input("Enter the name of the club hosting the event: ")

    _print_formatted_week_of_welcome(event_day_of_week, event_time, event_location, event_club_name)

    
#########################################

"""
Function Name: ramblinReck()
Parameters: N/A
Returns: None (NoneType)
"""

# ramblinReck helper functions:
def _calculate_ramblin_intensity(reck_distance: int) -> float:
    P = 10_000
    PI = 3.14

    return P / (4 * PI * (reck_distance ** 2))


def _print_formatted_ramblin_reck(ramblin_intensity: float) -> None:
     print(f"The Ramblin' Reck is {round(ramblin_intensity, ROUNDING_PRECISION)} Watts loud!")


# ramblinReck main function:
def ramblinReck() -> None:
    reck_distance = int(input("How far away are you from the Reck? "))

    ramblin_intensity = _calculate_ramblin_intensity(reck_distance)
    
    _print_formatted_ramblin_reck(ramblin_intensity)
   

#########################################

"""
Function Name: diningDollars()
Parameters: N/A
Returns: None (NoneTyoe)
"""

# diningDollars helper functions:
def _calculate_meal_cost() -> int:
    ITEM_COST_DICT = {
        "drink": 3,
        "appetizer": 6,
        "main course": 11,
        "dessert": 3
    }

    meal_cost = 0

    for item, cost in ITEM_COST_DICT.items():
        item_quantity = int(input(f"How many {item}s are you having? "))
        meal_cost += item_quantity * cost

    return meal_cost


def _calculate_total_cost_with_tip_and_remaining_dining_dollars(meal_cost: float) -> tuple[float, float]:
    INITIAL_DINING_DOLLARS = 23.0
    TIP_PERCENTAGE = 0.2

    total_cost_with_tip = (1 + TIP_PERCENTAGE) * meal_cost
    dining_dollars_in_account = INITIAL_DINING_DOLLARS - total_cost_with_tip

    return total_cost_with_tip, dining_dollars_in_account


def _print_formatted_dining_dollars(total_cost_with_tip: float, dining_dollars_in_account: float) -> None:
    print(f"You have spent a total of {round(total_cost_with_tip, ROUNDING_PRECISION)} dining dollars and have {round(dining_dollars_in_account, ROUNDING_PRECISION)} dining dollars left!")


# diningDollars main function:
def diningDollars() -> None:
    meal_cost = _calculate_meal_cost()

    total_cost_with_tip, dining_dollars_in_account = _calculate_total_cost_with_tip_and_remaining_dining_dollars(meal_cost)

    _print_formatted_dining_dollars(total_cost_with_tip, dining_dollars_in_account)


#########################################

"""
Function Name: findTs()
Parameters: N/A
Returns: None(NoneType)
"""

# findTs helper functions:
def _calculate_total_minutes_to_find_ts(number_of_places: int, number_of_people_searching: int) -> float:
    number_of_ts_total = number_of_places ** 2
    minutes_per_single_t = number_of_people_searching / 2

    return number_of_ts_total * minutes_per_single_t


def _get_hours_and_minutes_from_total_minutes(total_minutes: float) -> tuple[int, float]:
    hours = int(total_minutes // 60)
    minutes = total_minutes % 60

    return hours, minutes


def _print_formatted_find_ts(hours: int, minutes: float) -> None:
    print(f"It will take {hours} hour(s) and {round(minutes, ROUNDING_PRECISION)} minute(s) to find all of the T's!")


# findTs main function:
def findTs() -> None:
    number_of_places = int(input("How many locations do we need to search on campus? "))
    number_of_people_searching = int(input("How many people do we plan on searching with? "))

    total_minutes_to_find_ts = _calculate_total_minutes_to_find_ts(number_of_places, number_of_people_searching)

    hours_to_find_ts, minutes_remaining_to_find_ts = _get_hours_and_minutes_from_total_minutes(total_minutes_to_find_ts)

    _print_formatted_find_ts(hours_to_find_ts, minutes_remaining_to_find_ts)


#########################################

"""
Function Name: leftOverTime()
Parameters: N/A
Returns: None (NoneType)
"""

# leftOverTime helper functions:
def _calculate_remaining_free_time(credit_hours: int, sleep_hours_per_night: float, number_of_extracurriculars: int) -> int:
    TOTAL_WEEK_HOURS = 168

    education_time_per_week = 4 * credit_hours
    sleep_time_per_week = 7 * sleep_hours_per_night
    extracuricular_time_per_week = 4 * number_of_extracurriculars

    occupied_time = education_time_per_week + sleep_time_per_week + extracuricular_time_per_week

    return int(TOTAL_WEEK_HOURS - occupied_time)


def _print_formatted_left_over_time(remaining_free_time: int, free_time_activity: str) -> None:
    print(f"You have {remaining_free_time} hours this week to do {free_time_activity}.")


# leftOverTime main function:
def leftOverTime() -> None:
    credit_hours = int(input("How many credit hours are you taking? "))
    sleep_hours_per_night = float(input("How much sleep do you want to get each night? "))
    number_of_extracurriculars = int(input("How many extracurriculars do you participate in? "))
    free_time_activity = input("What activity do you want to do in your free time? ")

    remaining_free_time = _calculate_remaining_free_time(credit_hours, sleep_hours_per_night, number_of_extracurriculars)

    _print_formatted_left_over_time(remaining_free_time, free_time_activity)


#########################################