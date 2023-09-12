# Logistic映射是一种在动态系统中产生复杂行为的简单模型。
# 公式是x(k+1) = μ * x(k) * (1 - x(k))
# μ是控制参数，它决定了x随时间变化的速度和方式。
# 这个模型非常简单，但产生的行为却非常复杂。
#混沌Logistic映射的数学表达公式最早可以追溯到20世纪50年代，一些生态学家利用这个简单的差分方程来描述种群的变化。
#混沌Logistic映射具有极其复杂的动力学行为， 在保密通信等领域有广泛的应用。
#当μ的值在0到1之间时，x的值会逐渐收敛到0或1，这是系统的两个稳定状态。
#当μ的值大于1时，系统行为变得非常复杂，x的值会在两个不同的区间内来回变化，这是一个混沌状态。
#当 0<μ<=3.5699456时，Logistic呈现出周期性；
#当映射方程满足0<x0<1和3.5699456<μ<=4这两个条件时，x（k）在(0,1)。
#Logistic映射处于混沌状态，即一种无序的、不可预测的、混乱的、摸不到头、摸不到尾的状态。
#对给定的初始值x0，生成的序列是非周期性、非收敛以及对初始条件敏感的。
#而在其他取值范围之外，生成的序列则会收敛于某一个特定的值。

import matplotlib.pyplot as plt
try:
    mu = float(input("请输入mu的值："))
    x = float(input("请输入x的值："))
except ValueError:
    print("输入的值无效，请输入有效的数字。")
    exit()

# 为后续打印初始输入的x和mu暂存创设变量
initial_mu = mu
initial_x = x

def logistic_map(x, mu):
    return mu * x * (1 - x)

# 设定迭代次数和初始值
iterations = 1000
x_values = [x]

# 进行迭代
for i in range(iterations):
    x = logistic_map(x, mu)
    x_values.append(x)

# 绘制图形
plt.plot(x_values)
plt.xlabel('Iteration')
plt.ylabel('x')
plt.title('Logistic Map: x(t+1) = μ*x(t)*(1 - x(t))')
plt.text(0.5, -0.1, "μ control parameter = {}  x(0) = {}".format(initial_mu, initial_x), ha='center', va='center', transform=plt.gca().transAxes)
plt.show()
