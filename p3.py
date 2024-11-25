def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

# 範例輸入
n = 5
k = 2
result = josephus(n, k)
print(f"結果：{result}")
