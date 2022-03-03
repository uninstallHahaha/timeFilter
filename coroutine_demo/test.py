import gevent
import pandas as pd
from pandas import DataFrame, Series
import time

ret = {}


def read_sheet(reader, sheet_name: str) -> DataFrame:
    cur_sheet = reader.parse(sheet_name)
    ret[sheet_name] = cur_sheet
    return cur_sheet


if __name__ == '__main__':
    time_start = time.time()
    # 1. multi coroutine
    xl = pd.ExcelFile('../不同行为时间表-原始数据.xls')  # 14s
    sns = xl.sheet_names
    gsList = [gevent.spawn(read_sheet, xl, s_name) for s_name in sns]
    gevent.joinall(gsList)
    # 2. without coroutine
    # for sn in sns:
    #     pd.read_excel('../不同行为时间表-原始数据.xls', sheet_name=sn) # 149s
    # 2. read directly
    # xl = pd.read_excel('../不同行为时间表-原始数据.xls', sheet_name=None)  # 19s
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
