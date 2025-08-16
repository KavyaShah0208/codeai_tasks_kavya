import random

cards = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

def calculate_total(hand):
    total = 0
    aces = 0
    for card in hand:
        total += cards[card]
        if card == 'A':
            aces += 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

print("Welcome to blackjack")
balance = int(input("How much money would you like to deposit: "))

play = True

while play:
    if balance == 0:
        print("Your balance is 0. You can't continue playing.")
        break

    total = 0
    dealer_total = 0
    bet_possible = True
    print(f"Your balance is {balance} ")

    while bet_possible:
        bet = int(input("Enter bet amount: "))
        if bet <= balance:
            balance -= bet
            print(f"{bet} rupee bet placed, remaining balance is {balance}")
            bet_possible = False
        else:
            print("Bet exceeds balance amount. Try again.")

    card_labels = list(cards.keys())

    player = [random.choice(card_labels), random.choice(card_labels)]
    dealer = [random.choice(card_labels), random.choice(card_labels)]

    total = calculate_total(player)
    dealer_total = calculate_total(dealer)

    print(f"\nYour cards: {player}")
    print("Your total:", total)
    print(f"Dealer's first card is: {dealer[0]}")

    while dealer_total < 17:
        dealer.append(random.choice(card_labels))
        dealer_total = calculate_total(dealer)

    game_continue = True

    while game_continue:
        choice = input("Would you like to hit or stand: ").lower()

        if choice == 'hit':
            player.append(random.choice(card_labels))
            total = calculate_total(player)

            print(f"\nYour cards: {player}")
            print("Your total:", total)

            if total > 21:
                print("Total is above 21, you lose")
                game_continue = False
                next_round = input("Play another round (yes/no): ").lower()
                if next_round == 'yes':
                    game_continue = False
                else:
                    print(f"Alright, {balance} rupee withdrawn")
                    play = False
                    game_continue = False

            elif total == 21:
                print(f"Dealer's hand is {dealer}")
                print("You hit 21!")
                if total > dealer_total:
                    print(f"Congrats, you win {bet * 2}")
                    balance += bet * 2
                elif total == dealer_total:
                    print("It's a tie. Bet returned.")
                    balance += bet
                else:
                    print("Dealer wins.")
                print(f"Your balance is {balance}")
                next_round = input("Play another round (yes/no): ").lower()
                if next_round == 'yes':
                    game_continue = False
                else:
                    print(f"Alright, {balance} rupee withdrawn")
                    play = False
                    game_continue = False

        elif choice == 'stand':
            print(f"Dealer's hand is {dealer}")
            print(f"Dealer total is {dealer_total}")
            if dealer_total > 21:
                print(f"Congrats, you win {bet * 2}")
                balance += bet * 2
            elif dealer_total < total:
                print(f"Congrats, you win {bet * 2}")
                balance += bet * 2
            elif dealer_total > total:
                print("Dealer wins")
            else:
                print("It's a tie. Bet returned.")
                balance += bet

            print(f"Your balance is {balance}")
            next_round = input("Play another round (yes/no): ").lower()
            if next_round == 'yes':
                game_continue = False
            else:
                print(f"Alright, {balance} rupee withdrawn")
                play = False
                game_continue = False
