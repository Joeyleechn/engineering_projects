import os

DATA_ROOT = './data'
RAW_DATA_BASE_DIR = os.path.join(DATA_ROOT, 'inputs')
STRATEGY_BASE_DIR = os.path.join(DATA_ROOT, 'strategy')

RAW_ORGA_INPUT_DIR = os.path.join(RAW_DATA_BASE_DIR, 'OrgA')
ORGA_STRATEGY_DIR = os.path.join(STRATEGY_BASE_DIR, 'OrgA')
RAW_ORGA_INPUT_DIR = os.path.join(RAW_DATA_BASE_DIR, 'OrgB')
ORGB_STRATEGY_DIR = os.path.join(STRATEGY_BASE_DIR, 'OrgB')

Attribs = {
    'OrgA': {
        '10189': {
            'ProductName': 'GreatEquity',
            'Strategy_Dir': [ORGA_STRATEGY_DIR]
        }
    },
    'OrgB': {
        'FortuneF': {
            'AccountID': '25617',
            'Strategy_Dir': [ORGB_STRATEGY_DIR]
        }
    }
}