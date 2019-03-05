import random


class LineDel:
    def __init__(self):
        pass

    def get_del_ls(self, l_n, p_n, col_p=1):
        """
        :param l_n: 总行数
        :param p_n: 调节每次数据删除比例：0.05 * p_n
        :param col_p: 调节删除次数：默认col_p=1，70次左右
        :return: 所有待删除数据索引列表
        """
        res = []
        # 所有行数索引号
        all_data = list(range(0, l_n))
        # 将数据切割成 l_n / n_g 块, n_g: 每块数据区间的长度
        n_g = int(l_n * 0.48 / 10000 * col_p) - 1
        # 所有数据块的集合
        tar_n_g_ls = [all_data[i: i + int(l_n / n_g)] for i in range(0, l_n, int(l_n / n_g))]
        # 每个数据块中随机确定一个删除起点
        d_l = [random.sample(ls_, 1) for ls_ in tar_n_g_ls]
        # 数据删除起点列表 = 数据块数 l_n / n_g
        d_l = [i[0] for i in d_l]
        for n in d_l[:-1]:
            # 下一个待删除起点
            n_next_index = d_l.index(n) + 1
            n_next = d_l[n_next_index]
            # 每两个删除点之间取指定比例的数据删除 百分比: 0.05 * p_n
            per_dl = int((n_next - n) * 0.05 * p_n) + 1
            ls_tmp = [j for j in range(n, n + random.randrange(1, per_dl + 1))]
            # 所有待删除数据索引列表
            res += ls_tmp
        # 越界检查，删除越界部分
        if max(res) >= l_n:
            del_big_ls = list(range(l_n, max(res) + 1))
            res_ = set(res) - set(del_big_ls)
            res = list(res_)
        return res


if __name__ == '__main__':
    # test
    # 程序最终选择参数：l_n = 每个风机的总行数, p_n = 1, col_p=1
    for i in range(34):
        dd = LineDel()
        d = dd.get_del_ls(359800, 1)
        if max(d) > 359800:
            # 越界
            print('res wrong: %d' % max(d))
