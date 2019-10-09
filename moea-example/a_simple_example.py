"""使用一个moea多目标优化进化算法的框架，基于python的platypus，一个较完整的示例"""
from platypus import NSGAII, Problem, Real, GAOperator, SBX, PM, nondominated


class Belegundu(Problem):

    def __init__(self):
        # 定义决策变量，目标函数和约束的个数
        super(Belegundu, self).__init__(2, 2, 2)
        # 各个决策变量的取值范围
        self.types[:] = [Real(0, 5), Real(0, 3)]
        # 约束的形式
        self.constraints[:] = "<=0"
        # 可以定义各个目标函数是取最大值还是最小值
        self.directions[:] = [Problem.MINIMIZE, Problem.MINIMIZE]

    def evaluate(self, solution):
        # 可以把变量一个个取出，也可以数组直接赋值
        x = solution.variables[0]
        y = solution.variables[1]
        params = solution.variables
        # objectives是目标函数
        solution.objectives[:] = cal_fitness(params)
        # 定义解的约束
        solution.constraints[:] = [-x + y - 1, x + y - 7]


def fx1(params):
    x = params[0]
    y = params[1]
    return -2 * x + y


def fx2(params):
    x = params[0]
    y = params[1]
    return 2 * x + y


def cal_fitness(params):
    return [fx1(params), fx2(params)]


# 算法不仅可以用默认值，也可以指定种群数量，指定交叉(用的Variation表示交叉和变异，用Mutation表示变异)、变异等具体操作运算，
# 比如使用GAOperator，遗传算法算子，可以使用SBX做交叉重组运算和PM做变异运算。在具体的交叉变异函数里，定义相应的交叉率，交叉分布指数，变异率，变异分布指数等
algorithm = NSGAII(Belegundu(), population_size=500, variator=GAOperator(SBX(0.95, 20.0), PM(2, 25.0)))
# The final population could contain infeasible and dominated solutions if the number of function evaluations was
# insufficient (e.g. algorithm.Run(100)). In this case we would need to filter out the infeasible
# solutions:feasible_solutions = [s for s in algorithm.result if s.feasible]
# 即优化运算时，约束是软约束，所以运算代数太少，取得的值可能很多不在可行域内，因此如果是硬约束，能在初始化时约束好，就在初始化时进行约束。
algorithm.run(10000)

# plot the results using matplotlib
import matplotlib.pyplot as plt

# 展示所有解集
plt.scatter([s.objectives[0] for s in algorithm.result],
            [s.objectives[1] for s in algorithm.result])
plt.xlim([-10, 3])
plt.ylim([0, 13])
plt.xlabel("$f_1(x)$")
plt.ylabel("$f_2(x)$")
plt.show()

# we would need to filter out the infeasible solutions:只展示非劣解集
feasible_solutions = [s for s in algorithm.result if s.feasible]
plt.scatter([s.objectives[0] for s in feasible_solutions],
            [s.objectives[1] for s in feasible_solutions])
plt.xlim([-10, 3])
plt.ylim([0, 13])
plt.xlabel("$f_1(x)$")
plt.ylabel("$f_2(x)$")
plt.show()

# We could also get only the non-dominated solutions:可以只展示非劣解集
nondominated_solutions = nondominated(algorithm.result)
plt.scatter([s.objectives[0] for s in nondominated_solutions],
            [s.objectives[1] for s in nondominated_solutions])
plt.xlim([-10, 3])
plt.ylim([0, 13])
plt.xlabel("$f_1(x)$")
plt.ylabel("$f_2(x)$")
plt.show()

# 取出解集
# display the results
for solution in nondominated_solutions:
    # 目标值
    print(solution.objectives[0])
    # 对应的解集
    print(solution.variables[0])
    print(solution.variables[1])
