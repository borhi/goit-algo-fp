import random
from collections import Counter

import matplotlib.pyplot as plt

ROLLS = 1_000_000

ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(trials):
    counts = Counter(roll_dice() for _ in range(trials))
    probabilities = {
        total: counts.get(total, 0) / trials for total in range(2, 13)
    }
    return counts, probabilities


def print_probability_table(monte_carlo_probs, analytical_probs):
    print(f"\nРезультати симуляції ({ROLLS:,} кидків)\n")
    print(
        f"{'Сума':<8} {'Монте-Карло':<16} {'Аналітично':<16} {'Різниця':<12}"
    )
    print("-" * 56)

    for total in range(2, 13):
        mc = monte_carlo_probs[total] * 100
        an = analytical_probs[total] * 100
        diff = mc - an
        print(f"{total:<8} {mc:>6.2f}%{'':<9} {an:>6.2f}%{'':<9} {diff:>+6.2f}%")


def plot_probabilities(monte_carlo_probs, analytical_probs):
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] * 100 for s in sums]
    an_values = [analytical_probs[s] * 100 for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([i - width / 2 for i in x], mc_values, width, label="Монте-Карло", color="#1296F0")
    ax.bar([i + width / 2 for i in x], an_values, width, label="Аналітично", color="#F09612")

    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.set_xlabel("Сума на двох кубиках")
    ax.set_ylabel("Ймовірність (%)")
    ax.set_title(f"Ймовірності сум при {ROLLS:,} кидках (метод Монте-Карло)")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    counts, monte_carlo_probs = monte_carlo_simulation(ROLLS)
    print_probability_table(monte_carlo_probs, ANALYTICAL_PROBABILITIES)
    plot_probabilities(monte_carlo_probs, ANALYTICAL_PROBABILITIES)
