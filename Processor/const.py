import re
from enum import Enum, unique

UnKnown = 'UnKnown'

@unique
class ExchangeType(Enum):
    kSSE = 'a'
    kSZE = 'b'
    kunknown = UnKnown

@unique
class ExchangeFlag(Enum):
    kSSE = '0'
    kSZE = '1'
    kunknown = UnKnown

class ExchangeReg():
    SSE_A = re.compile('(6[0-9]{5})(.S(SE|H|SC))?$')
    SZE_A = re.compile('([0,3][0-9]{5})(.S(SE|H|SC))?$')
    CFEINDEX = re.compile('[H,HI][0-9]{6}(.CF(E|FEX))?$')