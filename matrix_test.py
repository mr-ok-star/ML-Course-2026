import torch

# 定义2x2矩阵A和B（float类型保证矩阵乘法精度）
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
B = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# 计算矩阵乘法（等价于 A @ B，区别于元素相乘A*B）
C = torch.matmul(A, B)

# 打印结果，验证是否符合线性代数规则
print("矩阵 A:\n", A)
print("矩阵 B:\n", B)
print("运算结果 C = A * B (矩阵乘法):\n", C)