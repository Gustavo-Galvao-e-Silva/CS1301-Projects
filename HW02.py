"""
Georgia Institute of Technology - CS1301
Homework 2 - Conditionals
"""

#########################################

"""
Function Name: buyTickets()
Parameters: num_people (int), ticket_section (str), days_before (int)
Returns: total_price (str)
"""
# Helper buyFunction methods
def _calcute_base_ticket_price(starting_price: float, ticket_section: str) -> float:
    ticket_section_multpliers = {
        'Loge': 1.5,
        'Courtside': 2.5 
    }

    base_price = 50.0 * ticket_section_multpliers.get(ticket_section, 1.0)

    print(f'Base price: ${base_price}/ticket')

    return base_price


def _add_late_purchase_fee(base_price: float, days_before: int) -> float:
    late_purchase_fee = 0.0

    if days_before <= 3:
        late_purchase_fee = 50
    elif days_before <= 7:
        late_purchase_fee = 20

    return base_price + late_purchase_fee


def _generate_total_price_string(number_of_people: int, final_ticket_price: float) -> str:
    total_price = number_of_people * final_ticket_price
    return f'The total for {number_of_people} people is: ${total_price}'



# Main buyFunction method
def buyTickets(num_people: int, ticket_section: str, days_before: int) -> str:
    base_price = _calcute_base_ticket_price(50.0, ticket_section)
    final_ticket_price = _add_late_purchase_fee(base_price, days_before)

    return _generate_total_price_string(num_people, final_ticket_price)


#########################################

"""
Function Name: matchStatus()
Parameters: player_games_won (int), opponent_games_won (int)
Returns: status (str)
"""

# Main matchStatus method
def matchStatus(player_games_won: int, opponent_games_won: int) -> str:
    if player_games_won == 6 and opponent_games_won == 6:
        return "Time for the tiebreak."
    
    game_difference = abs(player_games_won - opponent_games_won)
    
    if player_games_won >= 6 and game_difference >= 2:
        return "Player wins the set!"
    
    if opponent_games_won >= 6 and game_difference >= 2:
        return "Player loses the set."
    
    return "Set still in progress."


#########################################

"""
Function Name: tiebreak()
Parameters: player_1 (str), player_2 (str), score_1 (int), score_2 (int)
Returns: winner (str)
"""

# Main tieBreak method
def tiebreak(player_1: str, player_2: str, score_1: int, score_2: int):
    score_difference = abs(score_1 - score_2)
    print(f"Score gap: {score_difference}")

    if score_1 >= 6 and score_2 >= 6 and score_difference == 0:
        return "Tiebreak is intense!"
    elif score_1 >= 7 or score_2 >= 7 and score_difference >= 2:
        return f"{player_1 if score_1 > score_2 else player_2} wins the tiebreak!"      
    elif score_1 >= 6 or score_2 >= 6 and score_difference == 1:
        return f"{player_1 if score_1 > score_2 else player_2} is one point from winning!"  
    else:
        return "Tiebreak in progress!"


#########################################

"""
Function Name: playerStats()
Parameters: player_name (str), aces (int), double_faults (int), winners (int), unforced_errors (int)
Returns: player_performance (str)
"""

# Helper playerStats methods
def _calculate_player_scores(aces: int, double_faults: int, winners: int, unforced_errors: int) -> tuple[float]:
    serve_score = aces - 2 * double_faults
    rally_score = winners - unforced_errors
    return serve_score, rally_score


# Main playerStats method
def playerStats(player_name: str, aces: int, double_faults: int, winners: int, unforced_errors: int):
    serve_score, rally_score = _calculate_player_scores(aces, double_faults, winners, unforced_errors)

    if aces < 0 or double_faults < 0 or winners < 0 or unforced_errors < 0:
        return f"Invalid stats for {player_name}."
    
    elif serve_score >= 10 and rally_score >= 15:
        return f"{player_name} dominated the match! (Serve: {serve_score}, Rally: {rally_score})"
    
    elif serve_score >= 5 and rally_score >= 5:
        return f"{player_name} had an excellent match! (Serve: {serve_score}, Rally: {rally_score})"
    
    elif serve_score < 5 and rally_score < 5:
        return f"{player_name} struggled in this match. (Serve: {serve_score}, Rally: {rally_score})"
    
    else:
        return f"{player_name} had a mixed performance. (Serve: {serve_score}, Rally: {rally_score})"
    

#########################################

"""
Function Name: tennisPredictor()
Parameters: player_1 (str), player_2 (str), stats_1 (int), stats_2 (int), head_to_head (str), matches_played_1 (int), matches_played_2 (int)
Returns: prediction (str)
"""

# Main tennisPredictor method
def tennisPredictor(player_1: str, player_2: str, stats_1: int, stats_2: int, head_to_head: str, matches_played_1: int, matches_played_2: int) -> str:
    winner_string = "{} is predicted to win!"

    if stats_1 - stats_2 >= 15 and head_to_head == "P1" and matches_played_1 < 4:
        return winner_string.format(player_1)
    
    elif stats_2 - stats_1 >= 15 and head_to_head == "P2" and matches_played_2 < 4:
        return winner_string.format(player_2)
    
    elif stats_1 - stats_2 >= 15 and head_to_head != "P2" and stats_1 >= 70:
        return winner_string.format(player_1)
    
    elif stats_2 - stats_1 >= 15 and head_to_head != "P1" and stats_2 >= 70:
        return winner_string.format(player_2)
    
    elif abs(stats_1 - stats_2 <= 5) and head_to_head == "Tie" and matches_played_1 < matches_played_2:
        return winner_string.format(player_1)
    
    elif abs(stats_1 - stats_2 <= 5) and head_to_head == "Tie" and matches_played_2 < matches_played_1:
        return winner_string.format(player_2)
    
    elif abs(stats_1 - stats_2 <= 5) and head_to_head == "P1" and stats_1 >= 60:
        return winner_string.format(player_1)
    
    elif abs(stats_1 - stats_2 <= 5) and head_to_head == "P2" and stats_2 >= 60:
        return winner_string.format(player_2)
    
    else:
        return "Close match!"

#########################################


