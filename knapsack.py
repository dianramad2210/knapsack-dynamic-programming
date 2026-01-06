def knapsack_01_dp(weights, profits, capacity):
    n = len(weights)

    # Tabel DP
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Mengisi tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + profits[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking untuk mencari item terpilih
    w = capacity
    selected_items = []
    total_weight = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)  # item ke-i dipilih
            w -= weights[i - 1]
            total_weight += weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items, total_weight


# Data soal
weights = [1, 2, 3, 4, 5, 2, 6, 3, 4, 5]
profits = [6, 12, 18, 24, 30, 14, 36, 20, 26, 32]
capacity = 7

# Pemanggilan fungsi
max_profit, items, total_weight = knapsack_01_dp(weights, profits, capacity)

# Output
print("Nilai maksimum:", max_profit)
print("Daftar item terpilih:", items)
print("Total berat:", total_weight)
