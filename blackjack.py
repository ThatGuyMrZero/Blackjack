from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
game_ties = 0

# control the number of games the player will play
while game_continue:
    # print game number message
    game_num += 1
    print(f"START GAME #{game_num}")
    print()
    # deal a card to the player automatically
    player_hand = 0
    dealer_hand = 0
    # deal a card to the player
    card = rng.next_int(13) + 1
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10
    player_hand += card
    # add card number to the player hand value
    # print hand value
    print(f"Your hand is: {player_hand}")
    # keep playing the card game by prompting user to choose menu option
    no_winner = True
    while no_winner:
        # print four menu options
        # ask/prompt player for an input to choose a menu option
        print()
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()
        option = int(input("Choose an option: "))
        print()
        if option == 1:
            # deal another card to player
            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10
            player_hand += card
            # calculate the players hand
            print(f"Your hand is: {player_hand}")
            if player_hand == 21:
                print()
                print("BLACKJACK! You win!")
                print()
                player_wins += 1
                no_winner = False
            # if player hand == 21, print winning message
            elif player_hand > 21:
                print()
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                no_winner = False
            # elif player hand > 21, print losing message
            # update the number of games that player/dealer wins
        elif option == 2:
            # deal a card to the dealer
            dealer_card = rng.next_int(11) + 16
            dealer_hand += dealer_card
            # compare player hand value to dealer hand value
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()
            if player_hand > dealer_hand and player_hand <= 21:
                print("You win!")
                player_wins += 1
                print()
            elif dealer_hand > 21:
                print("You win!")
                player_wins += 1
                print()
            elif dealer_hand > player_hand and dealer_hand <=21:
                print("Dealer wins!")
                dealer_wins += 1
                print()
            elif player_hand == dealer_hand:
                print("It's a tie! No one wins!")
                game_ties += 1
                print()
            # determine who wins the game
            # update number of games player or dealer wins
            no_winner = False
        elif option == 3:
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_num - 1}")
            if game_num > 0:
                win_percentage = (player_wins / (game_num - 1)) * 100
                print(f"Percentage of Player wins: {win_percentage:.1f}%")
            # print stats: player_wins and dealer_wins information
        elif option == 4:
            # get outside of innerloop
            game_continue = False # get outside of outer loop
            no_winner = False
        else:
            # print invalid message
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
