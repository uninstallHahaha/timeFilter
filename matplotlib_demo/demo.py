import numpy as np
import matplotlib.pyplot as plt
from datetime import time, datetime

from dateutil import parser

# 设置字体, 默认中文显示不了
from matplotlib import rcParams

# 设置一个中文字体(楷体)
rcParams['font.sans-serif'] = 'KaiTi'
# 设置了中文字体后, 负号会显示不了, 设置这个属性使得负号可以显示
rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    t1: time = datetime(year=2021, month=1, day=10, hour=7, minute=30, second=0)
    t2: time = datetime(year=2021, month=1, day=10, hour=8, minute=0, second=0)
    ts = [t1, t2]
    parser.parse()
    vals = [10, 20]
    plt.plot(ts, vals)
    # print(t1, t2)
