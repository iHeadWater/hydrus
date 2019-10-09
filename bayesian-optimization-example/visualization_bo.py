"""bo优化过程的可视化"""
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import gridspec


def target(x):
    """在优化里，第一步都是优化目标的确定"""
    return np.exp(-(x - 2) ** 2) + np.exp(-(x - 6) ** 2 / 10) + 1 / (x ** 2 + 1)


x = np.linspace(-2, 10, 10000).reshape(-1, 1)
y = target(x)

plt.plot(x, y)
plt.show()

# 然后是构建BO对象，构建对象时需要目标函数，以及参数的取值范围，即定义要探索的参数空间.random_state是伪随机数生成器的种子
optimizer = BayesianOptimization(target, {'x': (-2, 10)}, random_state=27)

# maximize是执行寻优的函数，设置的参数包括随机探索的步数init_points,bo要执行的步数n_iter,以及提取函数权衡exploitation和exploration的参数kappa
optimizer.maximize(init_points=2, n_iter=0, kappa=5)


def posterior(optimizer, x_obs, y_obs, grid):
    """目标函数的函数（高斯过程）的后验分布"""
    optimizer._gp.fit(x_obs, y_obs)
    # 返回的mu和sigma应该是高斯分布的均值和方差平方根
    mu, sigma = optimizer._gp.predict(grid, return_std=True)
    return mu, sigma


def plot_gp(optimizer, x, y):
    """可视化高斯过程"""
    fig = plt.figure(figsize=(16, 10))
    steps = len(optimizer.space)
    fig.suptitle(
        'Gaussian Process and Utility Function After {} Steps'.format(steps),
        fontdict={'size': 30}
    )

    # 划分图形绘制的模块位置,2行1列
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    # gs[0]函数寻优绘制到上面，另一个提取函数相关的绘制在下面。
    axis = plt.subplot(gs[0])
    acq = plt.subplot(gs[1])

    x_obs = np.array([[res["params"]["x"]] for res in optimizer.res])
    y_obs = np.array([res["target"] for res in optimizer.res])
    # 求出新的mu和sigma
    mu, sigma = posterior(optimizer, x_obs, y_obs, x)
    axis.plot(x, y, linewidth=3, label='Target')
    axis.plot(x_obs.flatten(), y_obs, 'D', markersize=8, label=u'Observations', color='r')
    axis.plot(x, mu, '--', color='k', label='Prediction')
    # 绘制%95置信度的空间，就是均值附近1.96倍sigma
    axis.fill(np.concatenate([x, x[::-1]]),
              np.concatenate([mu - 1.9600 * sigma, (mu + 1.9600 * sigma)[::-1]]),
              alpha=.6, fc='c', ec='None', label='95% confidence interval')
    # 坐标方面相关的设置
    axis.set_xlim((-2, 10))
    axis.set_ylim((None, None))
    axis.set_ylabel('f(x)', fontdict={'size': 20})
    axis.set_xlabel('x', fontdict={'size': 20})
    # 效用函数（也就是acquisition function），用的是ucb，这个在几个常用的提取函数里简单，但是却比较好用.ucb用搞不到xi
    utility_function = UtilityFunction(kind="ucb", kappa=5, xi=0)
    # 调用效益函数进行计算
    utility = utility_function.utility(x, optimizer._gp, 0)
    acq.plot(x, utility, label='Utility Function', color='purple')
    acq.plot(x[np.argmax(utility)], np.max(utility), '*', markersize=15,
             label=u'Next Best Guess', markerfacecolor='gold', markeredgecolor='k', markeredgewidth=1)
    acq.set_xlim((-2, 10))
    acq.set_ylim((0, np.max(utility) + 0.5))
    acq.set_ylabel('Utility', fontdict={'size': 20})
    acq.set_xlabel('x', fontdict={'size': 20})

    axis.legend(loc=2, bbox_to_anchor=(1.01, 1), borderaxespad=0.)
    acq.legend(loc=2, bbox_to_anchor=(1.01, 1), borderaxespad=0.)


# 每一次优化都可视化其优化过程
plot_gp(optimizer, x, y)
plt.show()

optimizer.maximize(init_points=0, n_iter=1, kappa=5)
plot_gp(optimizer, x, y)
plt.show()

optimizer.maximize(init_points=0, n_iter=1, kappa=5)
plot_gp(optimizer, x, y)
plt.show()

optimizer.maximize(init_points=0, n_iter=1, kappa=5)
plot_gp(optimizer, x, y)
plt.show()

optimizer.maximize(init_points=0, n_iter=1, kappa=5)
plot_gp(optimizer, x, y)
plt.show()