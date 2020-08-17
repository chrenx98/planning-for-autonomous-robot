# tsp问题
class Solution:
    def __init__(self, X, start_node):
        self.X = X  # 距离矩阵
        self.start_node = start_node  # 开始的节点
        self.array = [[0] * (2 ** (len(self.X) - 1)) for i in range(len(self.X))]  # 记录处于x节点，未经历M个节点时，矩阵储存x的下一步是M中哪个节点

    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2 ** (s - 1)  # 二进制转换
        return su

    # tsp总接口
    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num))  # 形成节点的集合
        # past_sets = [s] #已遍历节点集合
        cities.pop(cities.index(s))  # 移除开始结点,构建未经历节点的集合
        node = s  # 初始节点
        return self.solve(node, cities)  # 求解函数

    def solve(self, node, future_sets):
        # 迭代终止条件，表示没有了未遍历节点，直接连接当前节点和起点即可
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 99999
        # node如果经过future_sets中节点，最后回到原点的距离
        distance = []
        # 遍历未经历的节点
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i)  # 删除第i个节点，认为已经完成对其的访问
            distance.append(self.X[node][s_i] + self.solve(s_i, copy))
        # 动态规划递推方程，利用递归
        d = min(distance)
        # node需要连接的下一个节点
        next_one = future_sets[distance.index(d)]
        # 未遍历节点集合
        c = self.transfer(future_sets)
        # 回溯矩阵，（当前节点，未遍历节点集合）——>下一个节点
        self.array[node][c] = next_one
        return d


def dynamic_programming_tsp(adjacent_matrix, start_city_number):
    """
    :param adjacent_matrix: 输入的邻接矩阵（距离矩阵）
    :param start_city_number: 这个数字指示了开始的城市在邻接矩阵里面的序号 从 0-k
    :return:
    """
    print("Using Dynamic Programming method(DP-method)")
    print("#####################################################################")
    D = adjacent_matrix
    S = Solution(D, start_city_number)
    print("Length of shortest path:", S.tsp())
    # 开始回溯
    M = S.array
    lists = list(range(len(S.X)))
    start = S.start_node
    print("The shortest loop is: ")
    while len(lists) > 0:
        lists.pop(lists.index(start))
        m = S.transfer(lists)
        next_node = S.array[start][m]
        print(start, "--->", next_node)
        start = next_node



