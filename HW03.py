"""
Georgia Institute of Technology - CS1301
Homework 3 - Iteration
"""

#########################################

"""
Function Name: decryptMessage()
Parameters: secretMessage (str)
Returns: finalTransmission (str)
"""

def decryptMessage(secretMessage: str) -> str:
    alien_symbols = "!@#()$%^&\*"
    
    num_alien_symbols = 0
    decrypted_message = ""

    for char in secretMessage:
        if char in alien_symbols:
            num_alien_symbols += 1
        else:
            decrypted_message += char

    return f"Message [{decrypted_message}] received. {num_alien_symbols} alien symbols found!"


#########################################

"""
Function Name: calculateFuel()
Parameters: operations (str), values (str), initialFuel (int)
Returns: finalFuel (str)
"""

def _update_remaining_fuel(current_fuel: int, value: int, operation: str) -> int:
    match operation:
        case '+':
            return current_fuel + value
        
        case '-':
            return current_fuel - value
        
        case '*':
            return current_fuel * value
        
        case '/':
            return current_fuel // value
        

def calculateFuel(operations: str, values: str, initialFuel: int) -> str:
    remaining_fuel = initialFuel

    for operation, value in zip(operations, values):
        remaining_fuel = _update_remaining_fuel(int(remaining_fuel), int(value), operation)

    return f"Mission success! Remaining fuel: {remaining_fuel}" if remaining_fuel >= 0 else "Mission failed: not enough fuel!"


#########################################

"""
Function Name: decodingData()
Parameters: data (str)
Returns: decodedData (str)
"""

def _generate_digit_groups(data: str) -> list[str]:
    groups = []
    temp_group = ""
    for i in range(len(data)):
        if i % 3 == 0 and i != 0:
            groups.append(temp_group)
            temp_group = ""

        temp_group += data[i]

    groups.append(temp_group)

    return groups


def _generate_decoded_string(groups: list[str]) -> str: 
    pi_digits = "314"
    ordered_digits = "123456789"

    decoded_string = ""
    for group in groups:
        decoded_string += group if group in ordered_digits else ""
        decoded_string += "pi" if group == pi_digits else ""

    return decoded_string if decoded_string else "No sequences found!"


def decodingData(data: str) -> str:
    groups = _generate_digit_groups(data)

    return _generate_decoded_string(groups)


#########################################

"""
Function Name: extinguishFire()
Parameters: password (str), maxTime (int)
Returns: outcome (str)
"""

def _calculate_remaining_time(password: str, maxTime: int) -> int:
    digit_time_consumption = {
        "aeiou": 2,
        "02468": 5
    }

    remaining_time = maxTime
    for char in password:
        for char_group, time_consumed in digit_time_consumption.items():
            remaining_time -= time_consumed if char in char_group else 0

    return remaining_time


def extinguishFire(password: str, maxTime: int) -> str:
    remaining_time = _calculate_remaining_time(password, maxTime)

    return f"Congrats! You have put out the fire with {remaining_time} minute(s) to spare!" if remaining_time >= 0 else "Oh no! I was too late to save the engine room!"


#########################################

"""
Function Name: dockAlign()
Parameters: corridor (str), limit (int)
Returns: dockingStatus (str)
"""

def _update_offset(char: str, offset: int) -> int:
    match char:
        case '<':
            return offset - 1
        
        case '>':
            return offset + 1
        
        case '=':
            return offset if offset == 0 else (offset - 1 if offset > 0 else offset + 1)
        
        case '!':
            return offset * 2
        
        case '[':
            return offset


def _offset_is_above_limit(offset: int, limit: int) -> bool:
    return abs(offset) > limit


def dockAlign(corridor: str, limit: int) -> str:
    offset = 0
    for i, char in enumerate(corridor):
        offset = _update_offset(char, offset)
        if _offset_is_above_limit(offset, limit):
            return f"Docking failed at position {i} (offset {offset})."
        
    return f"Docking was a complete success!" if offset == 0 else f"Docking complete with residual offset {offset}."


#########################################
