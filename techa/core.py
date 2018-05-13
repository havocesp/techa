# -*- coding:utf-8 -*-
import talib

import cycle
import experimental
import momentum
import overlap
import pattern
import prices
import statistic
import volatility
import volume

# from cycle import *
# from momentum import *
# from overlap import *
# from pattern import *
# from statistic import *
# from volatility import *
# from experimental import *
# from prices import *
# from volume import *

_function_list = [f for f in
                  (*cycle.__all__, *momentum.__all__, *overlap.__all__, *volatility.__all__, *pattern.__all__,
                   *statistic.__all__, *experimental.__all__, *prices.__all__) if f[0].isupper()]
__all__ = ['TaLib']


# noinspection SpellCheckingInspection
class TaLib:
    """
    Technical Analysis Library
    """

    _groups_ref = {
        'cycle': cycle.__all__,
        'momentum': momentum.__all__,
        'overlap': overlap.__all__,
        'patter': pattern.__all__,
        'statistic': statistic.__all__,
        'volume': volatility.__all__,
        'volatility': experimental.__all__,
        'price': prices.__all__,
        'experimental': volume.__all__
    }

    @classmethod
    def calculate_indicator(cls, indicator, *args, **kwargs):
        fn = globals().get(indicator)
        return fn(*args, **kwargs)

    @classmethod
    def get_groups(cls):
        """
        Just return groups names

        :return: groups names
        """

        return sorted([*cls._groups_ref])

    @classmethod
    def get_talib_groups(cls):
        """
        Just return groups names

        :return: groups names
        """
        return sorted([*talib.get_function_groups().keys()])

    @classmethod
    def get_functions(cls):
        """
        Return all functions supported by this lib

        :return: all functions supported by this lib
        """

        return sorted(sum(cls._groups_ref.values(), []))

    @classmethod
    def get_talib_functions(cls):
        """
        Return all functions supported by this lib

        :return: all functions supported by this lib
        """
        return sorted([*talib.get_function_groups().values()])


if __name__ == '__main__':
    print(TaLib.get_functions())
