#!/usr/bin/env python

import os
import pandas as pd 
from loguru import logger

from .base import Processor()
from .config import Attribs
from .const import (
    ExchangeReg,
    ExchangeType
)
from .utils import (
    get_exchange_by_code,
    gen_tmlist_by_exchange,
    find_partition_index,
    get_clean_code
)

class OrgBProcessor(Processor):

    def __init__(self, file_path) --> None:
        super(OrgBProcessor, self).__init__(
            'OrgB', file_path
        )
        self.__get_info_from_path()

    def __str__(self) -> str:
        logger.info(f'{self.product_name}, {self.account_id}, {self.date}')
    
    def __get_info_from_path(self) -> None:
        self.product_name = os.path.basename(
            self.file_path).split('-')[0]
        self.date = os.path.basename(
            self.file_path).split('-')[-1].split('.')[0]
        self.account_id = Attribs[self.account_id]['ProductName']
        self.__str__()

    def process_data(self) -> pd.DataFrame:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_raw = [line for line in f]
        begin = find_partition_index(
            data_raw,
            'Trading Details',
            'min'
        )
        end_tmp = find_partition_index(
            data_raw,
            'Report Info',
            'max'
        )
        end = find_partition_index(
            data_raw,
            self.date,
            'max'
        )
        columns = [''.join(i.split()) for i in data_raw[begin+1]]
        data_raw = data_raw[begin+2:end+1]
        data = pd.DataFrame(data=data_raw, columns=columns)
        data['Exchange'] = data['code'].apply(
            lambda x: get_exchange_by_code(x)
        )
        data['code'] = data['code'].apply(
            lambda x: get_clean_code(x)
        )
        return data
        