import logging


# set logging
def set_logging(path='log.txt', log_name='log', formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(path)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(f'')
    return logger


if __name__ == '__main__':
    logger_err = set_logging(path='error.txt', log_name='error')
    logger = set_logging()
    for i in range(10):
        if i == 5:
            try:
                res = int(None)
            except:
                logger_err.info('raise except...')
                continue
        logger.info(f'{i} ranging...')

    print('finish...')
