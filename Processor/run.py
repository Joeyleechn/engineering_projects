#!/usr/bin/ebv python
"""
Processor Runner

Usage:
    run.py [options]

Options:
    -h help               Show this screen
    -b --broker=<ORG>     Organization name input
    -d --date=<PATH>      Input date to process [default: None] 
"""

import os 
from docopt import docopt
from glob import glob
from loguru import logger

import cvt_io as io 
from Processor import (
    OrgAProcessor,
    OrgBProcessor
)