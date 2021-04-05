#!/usr/bin/ebv python
"""
Processor Runner

Usage:
    run.py [options]

Options:
    -h help               Show this screen
    -o --organization=<ORG>     Organization name input
    -d --date=<PATH>      Input date to process [default: None] 
"""

import os 
from docopt import docopt
from glob import glob
from loguru import logger

from .OrgA import OrgAProcessor
from .OrgB import OrgBProcessor
import config

def test_orga():
    files_paths = glob(f'{config.RAW_ORGA_INPUT_DIR}/*.csv')
    for file_path in files_paths:
        pcs = OrgAProcessor(file_path)
        res = pcs.process_data()
        print(res.head())

def test_orgb():
    files_paths = glob(f'{config.RAW_ORGA_INPUT_DIR}/*.txt')
    for file_path in files_paths:
        pcs = OrgBProcessor(file_path)
        res = pcs.process_data()
        print(res.head())

if __name__ == '__main__':
    args = docopt(__doc__)
    org = args['--organization']
    date = args['--date'] if args['--date'] is not None else '*' 
    print(f'>> test fir {org}')
    if org.lower() in ['orga', 'all']:
        test_orga()
    if org.lower() in ['orgb', 'all']:
        test_orgb()