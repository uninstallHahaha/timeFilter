import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import time
import random
import copy

from utils.sorts import Sorts


def gene_random_time(n: int):
    li = []
    for _ in range(n):
        hour = str(random.randint(0, 23))
        mini = str(random.randint(0, 59))
        sec = str(random.randint(0, 59))
        li.append(f'{hour.zfill(2)}:{mini.zfill(2)}:{sec.zfill(2)}')
    return li


def gene_random_type(n: int):
    li = []
    for _ in range(n):
        li.append(random.randint(1, 3))
    return li


if __name__ == '__main__':
    n: int = 800

    adf = DataFrame(data={
        'A': gene_random_time(n),
        'B': gene_random_time(n),
        'C': gene_random_type(n)
    })

    adf.to_excel(f'../range800.xlsx', header=False, index=False, index_label=None)

    sorted_adf = copy.deepcopy(adf)

    # 800 条: 6.5s
    time_start = time.time()
    Sorts.count = 0
    Sorts.fast_sort(sorted_adf, 0, adf.shape[0] - 1)
    time_end = time.time()
    print(f'{n}条完全无序数据排序耗时: {time_end - time_start} s, 共执行{Sorts.count}次递归')

    # 800 条: 65s
    s_start = time.time()
    Sorts.count = 0
    Sorts.fast_sort(sorted_adf, 0, adf.shape[0] - 1)
    s_end = time.time()
    print(f'{n}条严格排序数据排序耗时: {s_end - s_start} s, 共执行{Sorts.count}次递归')

    # 1000 条: 0.4s
    b_time = time.time()
    for i in range(sorted_adf.shape[0] - 2):
        flag: bool = sorted_adf.iloc[i].iloc[0] < sorted_adf.iloc[i + 1].iloc[0]
    be_time = time.time()
    print(f'遍历单调性耗时: {be_time - b_time} s')

    sorted_adf.to_excel('../range800_sorted.xlsx', header=False, index=False, index_label=None)
