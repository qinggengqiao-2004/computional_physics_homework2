import numpy as np

# 真实的 π 值（高精度）
true_pi = 3.141592653589793

# 指示函数 H(x,y): 如果 x² + y² ≤ 1 返回 1，否则 0
def H(x, y):
    return (x**2 + y**2 <= 1).astype(float)  # 向量化版本

# Monte Carlo 估计 π
def monte_carlo_pi(N, seed=None):
    # 随机种子
    rng = np.random.default_rng(seed)
    
    # 在 [-1, 1] x [-1, 1] 内均匀生成 N 个点
    x = rng.uniform(-1, 1, N)
    y = rng.uniform(-1, 1, N)
    
    # 计算落在单位圆内的点数
    hits = np.sum(H(x, y))
    
    # 积分近似值 I_N
    I_N = 4 * hits / N
    
    # 相对误差
    rel_error = abs(I_N - true_pi) / true_pi
    
    return I_N, rel_error

# 测试不同样本数 N 并输出结果

while True:
        try:
            user_input = input("Please input a seed (int number) to generate random numbers: ")
            seed = int(user_input)
        
            # 输入合法，跳出循环
            break
        
        except ValueError:
            print("错误：输入无效，请输入一个有效的整数！")


print("=== Monte Carlo 方法估计 π ===")
print(f"{'N':>12} {'I_N (≈π)':>18} {'相对误差':>15}")
print("-" * 50)

for N in [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]:
    I_N, err = monte_carlo_pi(N, seed)  # 固定 seed 使结果可复现
    print(f"{N:12d} {I_N:18.12f} {err:15.2e}")