import numpy as np
import matplotlib.pyplot as plt

def test8():
    # 假设的发动机转速与净转矩数据（单位：rpm，Nm）
    N_in = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000])  # 输入转速
    T_net = np.array([50, 150, 250, 350, 400, 380, 350])  # 净转矩

    # 拟合多项式（2次）
    coeff = np.polyfit(N_in, T_net, 2)  # 获取拟合系数
    T_net_fit = np.polyval(coeff, N_in)  # 计算拟合的净转矩
    print(T_net_fit)
    # 绘制发动机净转矩特性曲线
    plt.plot(N_in, T_net, 'ro', label='实验数据')  # 原始数据点
    plt.plot(N_in, T_net_fit, 'b-', label='拟合曲线')  # 拟合后的曲线
    plt.xlabel('输入转速 (rpm)')
    plt.ylabel('净转矩 (Nm)')
    plt.title('发动机净转矩特性曲线')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    test1()