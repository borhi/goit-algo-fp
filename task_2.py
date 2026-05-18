import math

import matplotlib.pyplot as plt

BRANCH_ANGLE = 45
LINE_COLOR = "#8B0000"


def draw_pythagoras_tree(ax, x, y, angle, length, depth):
    if depth == 0:
        return

    rad = math.radians(angle)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)

    ax.plot([x, x2], [y, y2], color=LINE_COLOR, linewidth=0.8)

    new_length = length * math.cos(math.radians(BRANCH_ANGLE))
    draw_pythagoras_tree(ax, x2, y2, angle + BRANCH_ANGLE, new_length, depth - 1)
    draw_pythagoras_tree(ax, x2, y2, angle - BRANCH_ANGLE, new_length, depth - 1)


def visualize_tree(depth):
    fig, ax = plt.subplots(figsize=(8, 10), facecolor="white")
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    ax.axis("off")

    draw_pythagoras_tree(ax, 0, 0, 90, 3, depth)

    ax.autoscale()
    ax.margins(0.08)
    ax.set_title(f"Дерево Піфагора (рівень рекурсії: {depth})")
    plt.tight_layout()
    plt.show()


def read_depth():
    while True:
        raw = input("Введіть рівень рекурсії (ціле число від 1 до 10): ").strip()
        try:
            depth = int(raw)
        except ValueError:
            print("Потрібно ввести ціле число.")
            continue
        if 1 <= depth <= 10:
            return depth
        print("Рівень має бути в діапазоні від 1 до 10.")


if __name__ == "__main__":
    level = read_depth()
    visualize_tree(level)
