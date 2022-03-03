import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import time

from utils.time_parser import time_parser
from utils.tools import swap_rows


class Sorts:
    count: int = 0

    # grid: 时间筛选表 DataFrame, 根据它的第一列数据排序
    @classmethod
    def fast_sort(cls, grid: DataFrame, l: int, r: int):
        cls.count += 1
        # print(f'inner id : {id(grid)}')
        if l < r:
            i: int = l
            j: int = r
            x = grid.iloc[i].iloc[0]
            tmp_row = grid.iloc[i]
            while i < j:
                while grid.iloc[j].iloc[0] > x and i < j:
                    j -= 1
                if i < j:
                    grid.iloc[i] = grid.iloc[j]
                    i += 1
                while grid.iloc[i].iloc[0] < x and i < j:
                    i += 1
                if i < j:
                    grid.iloc[j] = grid.iloc[i]
            grid.iloc[i] = tmp_row
            cls.fast_sort(grid, l, i - 1)
            cls.fast_sort(grid, i + 1, r)

    @classmethod
    def select_sort(cls, grid: DataFrame):
        n: int = grid.shape[0]
        for i in range(n):
            for j in range(i + 1, n):
                if grid.iloc[j].iloc[0] < grid.iloc[i].iloc[0]:
                    swap_rows(grid, i, j)


if __name__ == '__main__':
    pass
    # grid = DataFrame(data={'python': np.array([100, 100, 100, 100, 100]),
    #                      'math': np.array([200, 200, 200, 200, 200]),
    #                      'english': np.array([300, 300, 300, 300, 300])},
    #                index=list('ABCDE'))

    # grid = DataFrame(data={'python': np.random.randint(0, 150, size=5),
    #                      'math': np.random.randint(0, 150, size=5),
    #                      'english': np.random.randint(0, 150, size=5)},
    #                index=list('ABCDE'))

    # df = range_data = pd.read_excel('../range.xls', header=None)

    # grid = swap_rows(grid, x=0, y=1)
    # row = Series(data=np.random.randint(0, 150, size=3), index=['python', 'math', 'english'])
    # grid.iloc[0] = row

    # print(f'outter id : {id(grid)}')
    # fast_sort(df, 0, df.shape[0] - 1)
    # print(df)
