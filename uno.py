# Stephen Freeman and Alec Morin, we implemented the black wild cards and a bit of code for invalid move
import random

def start_game():
    
    colors = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))
    deck = [(rank, color) for rank in ranks for color in colors]
    deck += [("Wild", "Black")] * 4  
    
    random.shuffle(deck)

    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]
   
    print(f"Player 1 hand: {p1}")
    print(f"Player 2 hand: {p2}")
   
    central_card = deck.pop(0)
    print(f"Central card is: {central_card}")
   
    main_loop(p1, p2, deck, central_card, 0)
   
def main_loop(p1, p2, deck, central_card, whose_turn):
   
    while len(p1) > 0 and len(p2) > 0:
        
        current_hand = p1 if whose_turn == 0 else p2
        print(f"Player {whose_turn + 1}'s turn. Here is your hand: {current_hand}")
        print(f"Central card is: {central_card}")
       
        ans = int(input("You have a choice. Draw (0) or play (1): "))
       
        if ans == 1:
            
            player_choice = int(input("Which card to play? (1-based index): ")) - 1
            chosen_card = current_hand[player_choice]
           
            valid = valid_play(central_card, chosen_card)
           
            if valid:
                
                central_card = current_hand.pop(player_choice)
               
                if central_card[0] == "Wild":
                    new_color = input("You played a Wild card! Choose a new color (Red, Yellow, Green, Blue): ")
                    central_card = ("Wild", new_color)
            else:
                print("Invalid move! Try again.")
                continue 
               
        else:
            
            draw_card = deck.pop(0)
            current_hand.append(draw_card)
            print(f"You drew: {draw_card}")
       
        if len(current_hand) == 0:
            print(f"Player {whose_turn + 1} wins!")
            break
       
        if whose_turn == 0:
            p1 = current_hand  
        else:
            p2 = current_hand
       
        whose_turn = (whose_turn + 1) % 2
       
def valid_play(card1, card2):

    return card1[0] == card2[0] or card1[1] == card2[1] or card2[0] == "Wild"

start_game()
