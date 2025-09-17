"""
Georgia Institute of Technology - CS1301
Homework 4 - Strings
"""

#########################################

"""
Function Name: encodeMessage()
Parameters: message (str)
Returns: encoded_message (str)
"""

def encodeMessage(message: str) -> str:
    encoded_message = ""
    number_digits_removed = 0

    for ch in message:
        if not (ch.isdigit() or ch.isupper() or ch == ' '):
            encoded_message += ch
        
        number_digits_removed += 1 if ch.isdigit() else 0 

    return encoded_message[::-1] + f"{12 * number_digits_removed}"


#########################################

"""
Function Name: codeBreaker()
Parameters: message (str)
Returns: decoded_message (str)
"""

def codeBreaker(message: str) -> str:
    decoded_message = "" 
    
    for i, ch in enumerate(message):
        if i % 2 == 0: continue
        decoded_message += ' ' if ch == '_' else ch

    return decoded_message[:15]


#########################################

"""
Function Name: getCoordinates()
Parameters: location (str)
Returns: coordinates (str)
"""

def getCoordinates(location: str) -> str:
    coordinate_1 = location.lower().find('e')
    coordinate_2 = location[coordinate_1 + 1:].lower().find('e') + (coordinate_1 + 1)

    return f"Secret Lair Coordinates: ({coordinate_1 * 9}, {coordinate_2})"

#########################################

"""
Function Name: spyBudget()
Parameters: gadgets (str), budget (int)
Returns: cost_outcome (str)
"""

def spyBudget(gadgets: str, budget: int):
    gadget_prices = {
        'G': 25,
        'L': 15,
        'P': 30,
    }

    gadget_quantities = {
        'G': 0,
        'L': 0,
        'P': 0,
        'C': 0,
    }

    for gagdet in gadgets: 
        if gagdet == 'P' and gadget_quantities['P'] == 1:
            continue
        else:
            gadget_quantities[gagdet] += 1
            
    gadget_prices['C'] = 10 if gadget_quantities['C'] > 2 else 20

    mission_cost = 0

    for gadget, gadget_quantity in gadget_quantities.items():
        mission_cost += gadget_prices[gadget] * gadget_quantity

    return f"This mission will cost ${mission_cost - budget} too much!" if mission_cost > budget else "Ready for action!"


#########################################

"""
Function Name: findMole()
Parameters: suspect (str), codenames (str)
Returns: suspect_status (str)
"""

def findMole(suspect: str, codenames: str):
    name_last_char = suspect[-1].lower()
    codenames_list = codenames.split(':')


    for codename in codenames_list:
        if codename[-1].lower() == name_last_char:
            return f"{suspect}, codename {codename}, is a double agent!" if codename == codename[::-1] else f"{suspect}, codename {codename}, is not the mole."
    
    return f"{suspect} is still a suspect."

#########################################