# -*- coding: utf-8 -*-
"""
Python Technical Analysis library
"""
import talib
from collections import OrderedDict
from pprint import pprint

from talib.abstract import *
from finta import TA

from momentum import Momentum
from overlap import Overlap
from pattern import Pattern
from statistic import Statistic
from volatility import Volatility
from volume import Volume
from cycle import Cycle

__package__ = 'ta'
__author__ = 'Daniel J. Umpierrez'
__version__ = '0.0.1'

__all__ = ['TaLib', 'Statistic', 'Momentum', 'Volatility', 'Cycle', 'Pattern', 'Volume', 'TA']

# https://github.com/ranaroussi/qtpylib


class TaLib(TA, Momentum, Overlap, Pattern, Statistic, Volume, Cycle, Volatility):
    """
    Technical Analysis Library
    """

    @classmethod
    def get_groups(cls):
        groups = OrderedDict().fromkeys(sorted([grp for grp in cls.__dict__ if grp[0].isupper()]))
        for grp in groups:
            groups.update({grp: [fn for fn in cls.__dict__[grp].__dict__ if fn[0].isupper()]})
        return groups


    @classmethod
    def get_functions(cls):
        result = list()
        for grp in cls.get_groups().values():
            result.extend(grp)
        return sorted(result)

if __name__ == '__main__':
    # pprint(sorted([f for f in TA.__dict__.keys() if f[0].isupper()]))
    ta_func_list = [f for f in TA.__dict__ if f[0].isupper()]
    # TODO SMM SMMA PERCENT_B DMI MI VZO APZ
    talib_func_list = talib.get_functions()
    # for func in ta_func_list:
    #     if func not in talib_func_list and func not in ['KST', 'VWAP', 'FISH', 'ER', 'ZLEMA', 'QSTICK', 'TSI', 'VORTEX', 'EMV', 'WTO', 'EBBP' , 'HMA', 'VAMA', 'PIVOTS', 'CFI', 'WOBV', 'COPP', 'ICHIMOKU', 'CHAIKIN', 'BASP', 'BASPN', 'BUYP', 'SELLP', 'BUYPN', 'SELLPN', 'AO', 'UO', 'WILLIAMS', 'STOCHD', 'CHANDELIER', 'EFI', 'DO', 'KC', 'IFT_RSI', 'TP', 'ADL', 'TR']:
    #         print(func)
    for fn in sorted(talib.get_functions()):
        params = Function(fn).parameters
        if len(params):
            print(fn, ': ', *['{} = {}'.format(k, v) for k, v in params.items()])

    # for fn in [f for f in TA.__dict__ if f.isupper()]:
    #
    #     print(getattr(TA, fn).__doc__)
