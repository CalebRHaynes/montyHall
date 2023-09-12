import random
import matplotlib.pyplot as plt


def simulate_monty_hall(switch=0):
    prizes = [0, 0, 1]
    random.shuffle(prizes)
    player_choice = random.randint(0, 2)
    remaining_goats = [i for i, prize in enumerate(prizes) if prize == 0 and i != player_choice]
    # Monty, show that door!
    door_to_reveal = random.choice(remaining_goats)
    if switch:
        player_choice = 3 - player_choice - door_to_reveal
    outcome = prizes[player_choice]

    return outcome  # 1 for a win, 0 for lose


if __name__ == '__main__':
    num_simulations = 100000000

    # Switching strategy, pick door, always switch
    switch_wins = 0
    for _ in range(num_simulations):
        result = simulate_monty_hall(switch=1)
        switch_wins += result
    print(f"Out of {num_simulations} simulations, the player won {switch_wins} times switching.")

    # Stay strategy, pick door, never switch
    stay_wins = 0
    for _ in range(num_simulations):
        result = simulate_monty_hall(switch=0)
        stay_wins += result
    print(f"Out of {num_simulations} simulations, the player won {stay_wins} times staying.")

    fig, ax = plt.subplots()

    strats = ['switch', 'stay']
    counts = [switch_wins, stay_wins]
    bar_labels = ['stay', 'switch']
    bar_colors = ['tab:red', 'tab:blue']

    ax.bar(strats, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel('Number of Wins')
    ax.set_title(f'Strategy n={num_simulations} iter')
    ax.legend(title='Strategy')

    plt.savefig("simulated.png")
