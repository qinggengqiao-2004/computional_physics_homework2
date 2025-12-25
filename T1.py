import numpy as np

# 真实的 π 值（高精度）
true_pi = 3.141592653589793

# 被积函数
def f(x):
    return 4 / (1 + x**2)

# (a) 梯形法则
def trapezoidal(n):
    h = 1.0 / n
    x = np.linspace(0, 1, n + 1)
    y = f(x)
    I = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))  # 梯形公式
    rel_error = abs(I - true_pi) / true_pi
    return I, rel_error

# (b) 辛普森法则（要求 n 为偶数）
def simpson(n):
    if n % 2 != 0:
        raise ValueError("对于辛普森法则，n 必须是偶数")
    h = 1.0 / n
    x = np.linspace(0, 1, n + 1)
    y = f(x)
    # 辛普森公式
    I = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[-1])
    rel_error = abs(I - true_pi) / true_pi
    return I, rel_error

# 测试不同 n 值并输出结果
print("=== 梯形法则 (Trapezoidal rule) ===")
for n in [10, 50, 100, 500, 1000, 5000, 10000]:
    I, err = trapezoidal(n)
    h = 1.0 / n
    print(f"n = {n:5d}, h = {h:.6f}, I ≈ {I:.12f}, 相对误差 = {err:.2e}")

print("\n=== 辛普森法则 (Simpson's rule) ===")
for n in [10, 20, 50, 100, 200, 500, 1000]:
    I, err = simpson(n)
    h = 1.0 / n
    print(f"n = {n:5d}, h = {h:.6f}, I ≈ {I:.12f}, 相对误差 = {err:.2e}")