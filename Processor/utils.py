import os
import re
import pandas as pd 
from loguru import logger

DATA_ROOT = './data'

from .const import (
    ExchangeReg,
    ExchangeType,
    ExchangeFlag
)


def get_exchange_by_code(code: str) -> str:
    if code.isnumeric():
        code = code.zfill(6)
    if re.match(ExchangeReg.SSE, code):
        exchange = ExchangeType.kSSE.value
    elif re.match(ExchangeReg.SZE, code):
        exchange = ExchangeType.kSZE.value
    else:
        exchange = ExchangeType.kunknown.value
        logger.warning(f'Code: {code}, Exchange: {exchange}')


def gen_tmlist_by_exchange(
    STRATEGY_BASE_DIR: str,
    product_name: str,
    data: str,
    length: int,
    format: str
) -> list:
    json = pd.read_json(os.path.join(
        STRATEGY_BASE_DIR, product_name, data, 'trade_equity.json'
    )).iloc[0,0]
    start_time = ' '.join([date, json['args']['start_time']])
    end_time = ' '.join([date, json['args']['end_time']])
    timestamp = pd.date_range(start_time, end_time, length)
    try:
        timestamp = [time.strftime(format) for time in timestamp]
    except Exception as e:
        logger.warning(f'Not supported format[{format}]m {e}')
        raise e 
    return timestamp


def find_partition_index(
    partition_src: list,
    key_word: str,
    method, str
) -> int:
    """[locate the desired information]
    
    Args:
        partition_src: where to find
        key_word: symbol
        method: ['min', 'max'] for head or tail respectively
    """
    word_index = None
    if method == 'min':
        word_index = min([
            i for i in range(len(partition_src))
            if key_word in partition_src[i]
        ])
        if not word_index:
            logger.error(f'{key_word} not found')
            raise ValueError
    elif method == 'max':
        word_index = max([
            i for i in range(len(partition_src))
            if key_word in partition_src[i]
        ])
        if not word_index:
            logger.error(f'{key_word} not found')
            raise ValueError
    else:
        logger.error(f'{method} not supported')
            raise ValueError
    return word_index
    
