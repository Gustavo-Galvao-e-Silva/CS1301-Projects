# Program constants
PI = 3.14
ROUNDING_PRECISION = 2

# ====================================================================================

# techLibs helper functions
def _get_tech_libs_input() -> tuple[str]:
    name = input("Enter your name: ")
    friend_name = input("Enter your best friend's name: ")
    favorite_study_spot = input("Enter your favorite study spot: ")

    return name, friend_name, favorite_study_spot


def _print_tech_libs(name: str, friend_name: str, favorite_study_spot: str) -> None:
    print(f"The other day, I saw {name} and {friend_name} up to no good.")
    print(f"They were loudly gossiping at {favorite_study_spot} instead of studying.")


# techLibs main function
def techLibs() -> None:
    name, friend_name, favorite_study_spot = _get_tech_libs_input()
    _print_tech_libs(name, friend_name, favorite_study_spot)


# ====================================================================================

# diningDollars helper functions
def _get_dining_dollars_input() -> tuple[float, float, int]:
    balance = float(input("How many dining dollars do you currently have? "))
    weekly_expenditure = float(input("How many dining dollars do you spend per week? "))
    weeks_left = int(input("How many weeks are left? "))

    if balance < 0 or weekly_expenditure < 0 or weeks_left < 0:
        raise ValueError("Inputs can't be negative")

    return balance, weekly_expenditure, weeks_left


def _calculate_remaining_balance(balance: float, weekly_expenditure: float, weeks_left: int) -> float:
    return round(balance - weekly_expenditure * weeks_left, ROUNDING_PRECISION)


def _print_dining_dollars(remaining_balance: float) -> None:
    print(f"You will have ${remaining_balance} left over.")


# diningDollars main function
def diningDollars() -> None:
    balance, weekly_expenditure, weeks_left = _get_dining_dollars_input()
    remaining_balance = _calculate_remaining_balance(balance, weekly_expenditure, weeks_left)
    _print_dining_dollars(remaining_balance)


# ==================================================================================== 

# sphereVol helper functions
def _get_radius_input() -> float:
    radius = float(input("Enter the radius of your sphere: "))

    if radius < 0:
        raise Exception("Radius can't be negative")

    return radius


def _calculate_sphere_volume(radius: float) -> float:
    return round(4/3 * PI * (radius ** 3), ROUNDING_PRECISION)


def _print_sphere_vol(sphere_volume: float) -> None:
    print(f"The volume of your sphere is {sphere_volume}.")


# sphereVol main function
def sphereVol() -> None:
    radius = _get_radius_input()
    sphere_volume = _calculate_sphere_volume(radius)
    _print_sphere_vol(sphere_volume)


# ==================================================================================== 

# italianNight main function
def italianNight(cookTime: float) -> str:
    cook_times = {
        "Breadsticks": 20,
        "Pasta": 35,
        "Lasagna": 50
    }

    longest_dish = ""

    for dish, dish_cook_time in cook_times.items():
        