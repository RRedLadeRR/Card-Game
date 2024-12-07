import random

# Створюємо колоду карт (від 2 до Туза)
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♥', '♦', '♣']
    return [(rank, suit) for rank in ranks for suit in suits]

# Присвоєння ваги для карт (для порівняння)
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

# Перетасування колоди
def shuffle_deck(deck):
    random.shuffle(deck)

# Гра в один раунд
def play_round(player1, player2, deck):
    # Витягуємо карти для гравців
    card1 = deck.pop()
    card2 = deck.pop()
    
    print(f"{player1} витягує карту {card1[0]}{card1[1]}")
    print(f"{player2} витягує карту {card2[0]}{card2[1]}")
    
    # Порівняння карт і визначення переможця раунду
    if card_values[card1[0]] > card_values[card2[0]]:
        print(f"{player1} виграє раунд!\n")
        return player1
    elif card_values[card1[0]] < card_values[card2[0]]:
        print(f"{player2} виграє раунд!\n")
        return player2
    else:
        print("Нічия в раунді!\n")
        return None

# Основна гра
def play_game():
    print("Вітаємо у грі 'Війна'!")
    player1 = input("Введіть ім'я першого гравця: ")
    player2 = input("Введіть ім'я другого гравця: ")
    
    # Створюємо і перетасовуємо колоду
    deck = create_deck()
    shuffle_deck(deck)
    
    # Підрахунок балів
    scores = {player1: 0, player2: 0}
    
    # Гра в кілька раундів
    num_rounds = int(input("Скільки раундів ви хочете зіграти? "))
    for i in range(num_rounds):
        print(f"\nРаунд {i + 1}")
        winner = play_round(player1, player2, deck)
        if winner:
            scores[winner] += 1
    
    # Підсумки гри
    print("\nРезультати гри:")
    print(f"{player1}: {scores[player1]} очок")
    print(f"{player2}: {scores[player2]} очок")
    
    if scores[player1] > scores[player2]:
        print(f"{player1} перемагає у грі!")
    elif scores[player1] < scores[player2]:
        print(f"{player2} перемагає у грі!")
    else:
        print("Гра закінчилася внічию!")

# Запуск гри
if __name__ == "__main__":
    play_game()
