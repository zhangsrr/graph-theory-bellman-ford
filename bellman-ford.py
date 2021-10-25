# Created by Zhang Siru at 2021/10/22 15:19 with PyCharm
# Feature: Using Bellman-Ford Algorithm to find the shortest path or secondary shortest path
# Python Version: 3.6
# ResourceFile: ./data/graphgenerated.csv

"""
Bellman-Ford Algorithm:
已知点边关系
用邻接矩阵求解？可以
如何处理Pr(v)的选择问题？先读完文件，可以获得顶点数，再从中随机选择一个，[实验过程可以换成for循环遍历每一个可能的源点]
初始化随机选择点？直接指定0？同上
考虑负权重，如何初始化∞的cost？float['inf']

"""


import os
import pandas as pd


def read_file(filename):
    """
    :param filename: data_path
    :return: [[id, source, target, cost]...[]] (2-d array)
    """
    data_frame = pd.read_csv(filename)
    print(data_frame.values)  # each numpy array represents [id, source, target, cost]
    # print(data_frame.values[0][0])
    return data_frame.values





if __name__ == '__main__':
    data_folder = os.getcwd() + '\\data'
    data_path = os.path.join(data_folder, os.listdir(data_folder)[0])  # 这两行可以简化
    read_file(filename=data_path)

