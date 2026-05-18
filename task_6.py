items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def _totals(selected, menu):
    total_cost = sum(menu[name]["cost"] for name in selected)
    total_calories = sum(menu[name]["calories"] for name in selected)
    return total_cost, total_calories


def greedy_algorithm(menu, budget):
    ranked = sorted(
        menu.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected = []
    remaining = budget

    for name, data in ranked:
        if data["cost"] <= remaining:
            selected.append(name)
            remaining -= data["cost"]

    total_cost, total_calories = _totals(selected, menu)
    return {
        "items": selected,
        "cost": total_cost,
        "calories": total_calories,
        "budget_left": budget - total_cost,
    }


def dynamic_programming(menu, budget):
    names = list(menu.keys())
    costs = [menu[name]["cost"] for name in names]
    calories = [menu[name]["calories"] for name in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = costs[i - 1]
        calorie = calories[i - 1]
        for w in range(budget + 1):
            without = dp[i - 1][w]
            with_item = dp[i - 1][w - cost] + calorie if w >= cost else 0
            dp[i][w] = max(without, with_item)

    remaining = budget
    selected = []
    for i in range(n, 0, -1):
        if dp[i][remaining] != dp[i - 1][remaining]:
            selected.append(names[i - 1])
            remaining -= costs[i - 1]

    selected.reverse()
    total_cost, total_calories = _totals(selected, menu)
    return {
        "items": selected,
        "cost": total_cost,
        "calories": total_calories,
        "budget_left": budget - total_cost,
    }


def print_result(title, result, budget):
    print(f"\n{title}")
    print(f"  Бюджет: {budget}")
    print(f"  Обрані страви: {', '.join(result['items']) if result['items'] else '—'}")
    print(f"  Витрачено: {result['cost']}")
    print(f"  Залишок: {result['budget_left']}")
    print(f"  Калорійність: {result['calories']}")


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print_result("Жадібний алгоритм (калорії / вартість)", greedy_result, budget)
    print_result("Динамічне програмування (оптимально)", dp_result, budget)
