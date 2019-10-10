"""advanced 操作"""

from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction


# Let's start by definying our function, bounds, and instanciating an optimization object.
def black_box_function(x, y):
    """定义目标函数"""
    return -x ** 2 - (y - 1) ** 2 + 1


# 实例化bo
optimizer = BayesianOptimization(
    f=None,
    pbounds={'x': (-2, 2), 'y': (-3, 3)},
    verbose=2,
    random_state=1,
)

# 使用效用函数
utility = UtilityFunction(kind="ucb", kappa=2.5, xi=0.0)

next_point_to_probe = optimizer.suggest(utility)
print("Next point to probe is:", next_point_to_probe)

target = black_box_function(**next_point_to_probe)
print("Found the target value to be:", target)

optimizer.register(
    params=next_point_to_probe,
    target=target,
)


# 下面是处理离散参数的手段。 “//”运算符是向下取整的操作
def func_with_discrete_params(x, y, d):
    # Simulate necessity of having d being discrete.
    assert type(d) == int

    return ((x + y + d) // (1 + d)) / (1 + (x + y) ** 2)


def function_to_be_optimized(x, y, w):
    """w是要离散化的，用int强行离散化了"""
    d = int(w)
    return func_with_discrete_params(x, y, d)


optimizer = BayesianOptimization(
    f=function_to_be_optimized,
    pbounds={'x': (-10, 10), 'y': (-10, 10), 'w': (0, 5)},
    verbose=2,
    random_state=1,
)

optimizer.maximize(alpha=1e-3)

# 调整高斯回归
optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds={'x': (-2, 2), 'y': (-3, 3)},
    verbose=2,
    random_state=1,
)
optimizer.maximize(
    init_points=1,
    n_iter=5,
    # What follows are GP regressor parameters
    alpha=1e-3,
    n_restarts_optimizer=5
)
optimizer.set_gp_params(normalize_y=True)
