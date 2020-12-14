import os
import pandas as pd
from loguru import logger
from .config import var

class Processor():
    '''
    Transform unstructured data into clean data.
    '''
    def __init__(
        self, org_name: str, file_path: str
    ) -> None:
        self.org_name = org_name
        self.file_path = file_path
