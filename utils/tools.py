from pandas import DataFrame, Series
from functools import reduce
import numpy as np
import pandas as pd


# x, y : rows indexes to exchange, begin with 0
def swap_rows(df: DataFrame, x: int, y: int) -> DataFrame:
    return df.iloc[:x] \
        .append(df.iloc[y:y + 1], ) \
        .append(df.iloc[x + 1:y]) \
        .append(df.iloc[x:x + 1]) \
        .append(df.iloc[y + 1:])


# check monotonicity
def check_mono(df: DataFrame) -> bool:
    res: bool = True
    for i in range(df.shape[0] - 2):
        if df.iloc[i].iloc[0] > df.iloc[i + 1].iloc[0]:
            res = False
            break
    return res


# set DataFrame's index to '---time----'
def update_df_col(df: DataFrame, loc: int, name='time') -> bool:
    if df is None:
        return False
    cols = ['-'] * df.shape[1]
    # continue if the sheet is not content time column
    if len(cols) < loc:
        return False
        # set the filter column's name to 'time'
    cols[loc - 1] = name
    df.columns = cols
    df.index = map(lambda x: x, range(0, df.shape[0]))
    return True


# slice the list of dataFrame to smell bucket, return more delicate list
def sliceList(origin: list, bucket: int) -> list:
    total = reduce(lambda x, y: pd.concat([x, y], axis=0), origin)
    ret_list = []
    loc = 0
    while loc + bucket <= total.shape[0]:
        ret_list.append(total.iloc[loc:loc + bucket])
        loc += bucket
    if loc < total.shape[0]:
        ret_list.append(total.iloc[loc:])
    return ret_list
