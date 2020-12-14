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

class OrgAProcessor(Processor):

    def __init__(self, file_path) --> None:
        super(OrgAProcessor, self).__init__(
            'OrgA', file_path
        )
        self.product_name = None
        self.account_id = None
        self.date = None

    def __str__(self) -> str:
        logger.info(f'{self.product_name}, {self.account_id}, {self.date}')
    
    def __get_info_from_path(self):
        self.account_id = os.path.basename(
            self.file_path).solit('-')[0]
        self.date = os.path.basename(
            self.file_path).solit('-')[-1].split('.')[0]
        self.product_name = Attribs[self.account_id]['ProductName']
        self.__str__()

    def process_data(self):
        self.__get_info_from_path()
        data_raw = pd.read_csv(self.file_path)
        begin = find_partition_index(
            data_raw.iloc[:, 0].fillna('').tolist(),
            'Trading Details',
            'min'
        )
        end_tmp = find_partition_index(
            data_raw.iloc[:, 0].fillna('').tolist(),
            'Report Info',
            'max'
        )
        end = find_partition_index(
            data_raw.iloc[begin:end_tmp, 0].fillna('').tolist(),
            self.date,
            'max'
        )
        columns = data_raw.iloc[begin+1, :].values

        data = data_raw.iloc[begin+2:end+1, :].reset_index(drop=True)
        data.columns = columns
        