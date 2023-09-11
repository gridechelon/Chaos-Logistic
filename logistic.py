import matplotlib.pyplot as plt

# Logistic映射是一种在动态系统中产生复杂行为的简单模型。
# 公式是x(t+1) = μ * x(t) * (1 - x(t))
# μ是控制参数，它决定了x随时间变化的速度和方式。
# 这个模型非常简单，但产生的行为却非常复杂。
# 当μ的值在0到1之间时，x的值会逐渐收敛到0或1，这是系统的两个稳定状态。
# 然而，当μ的值大于1时，系统行为变得非常复杂，x的值会在两个不同的区间内来回变化，这是一个混沌状态。
#混沌Logistic是一种混沌映射，通过迭代产生混沌序列。
# 这个映射方程是Logistic方程，形式为Xn+1=μ×Xn×(1-Xn)，其中μ是Logistic参数，取值范围在[0,4]。
#混沌Logistic映射的数学表达公式最早可以追溯到20世纪50年代，一些生态学家利用这个简单的差分方程来描述种群的变化。

#混沌Logistic映射具有极其复杂的动力学行为， 在保密通信等领域有广泛的应用。
# 当μ取值在3.57至4之间时，混沌Logistic映射处于完全混沌状态，生成的序列是非周期的、不收敛的。
# 而在其他取值范围之外，生成的序列则会收敛于某一个特定的值。

try:
    mu = float(input("请输入mu的值："))
    x = float(input("请输入x的值："))
except ValueError:
    print("输入的值无效，请输入有效的数字。")
    exit()

#print("Logistic映射的混沌行为,μ是控制参数(0,1),[1,4),[4,)")
#mu = float(input("请输入mu的值："))
#x = float(input("请输入x的值："))

# 打印初始的x和mu
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
