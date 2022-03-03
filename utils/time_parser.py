import time


# str to datetime.time
def time_parser(value: str) -> time:
    if value == '':
        return ''
    ts = value.split(':')
    if len(ts[2].split('.')) > 1:
        mill_second = int(ts[2].split('.')[1])
    else:
        mill_second = 0

    refer_time = time(int(ts[0]), int(ts[1]), int(ts[2].split('.')[0]), mill_second)
    return refer_time
