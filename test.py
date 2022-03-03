import sys
import time
from tqdm import tqdm

# pbar = tqdm(["a", "b", "c", "d"])
# for char in pbar:
#     pbar.set_description("Processing %s" % char)
# with tqdm(total=100) as pbar:
#     pbar.set_description("正在处理 ")
#     for i in range(10):
#         time.sleep(1)
#         pbar.update(10)

import time
import threading
from openpyxl import load_workbook


class Loading(threading.Thread):
    list_b = ['loading.', 'loading..', 'loading...', 'loading....', 'loading    ']
    ld = True

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        while self.ld:
            for i in self.list_b:
                print('%s\r' % i, end='')
                time.sleep(0.2)


