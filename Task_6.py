items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_calories += info['calories']
            total_cost += info['cost']
        else:
            break

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(names)

    # Ініціалізуємо матрицю для зберігання максимальних калорій на кожен бюджет
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо матрицю dp
    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    # Визначаємо обрані страви
    total_calories = dp[n][budget]
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(names[i - 1])
            j -= costs[i - 1]

    selected_items.reverse()  
    total_cost = sum(items[item]['cost'] for item in selected_items)
    return selected_items, total_calories, total_cost

# Приклад використання
budget = 100
print("Greedy Algorithm:")
selected_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
print("Selected items:", selected_items_greedy)
print("Total calories:", total_calories_greedy)
print("Total cost:", total_cost_greedy)

print("\nDynamic Programming:")
selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print("Selected items:", selected_items_dp)
print("Total calories:", total_calories_dp)
print("Total cost:", total_cost_dp)
