# -*- coding:utf-8 -*-
import importlib

_groups_functions = {
    'cycle': [d for d in dir(importlib.import_module('cycle')) if d[0].isupper()],
    'momentum': [d for d in dir(importlib.import_module('momentum')) if d[0].isupper()],
    'overlap': [d for d in dir(importlib.import_module('overlap')) if d[0].isupper()],
    'pattern': [d for d in dir(importlib.import_module('pattern')) if d[0].isupper()],
    'statistic': [d for d in dir(importlib.import_module('statistic')) if d[0].isupper()],
    'volume': [d for d in dir(importlib.import_module('volume')) if d[0].isupper()],
    'volatility': [d for d in dir(importlib.import_module('volatility')) if d[0].isupper()],
    'price': [d for d in dir(importlib.import_module('prices')) if d[0].isupper()],
    'experimental': [d for d in dir(importlib.import_module('experimental')) if d[0].isupper()]
}

_function_list = sum([k for k in _groups_functions.values()], [])

__all__ = ['TaLib'] + _function_list


# noinspection SpellCheckingInspection
class TaLib:
    """
    Technical Analysis Library
    """

    # Possible values: [ "talib" | "finta" ]
    # This attribute set a technical library as primary so the setted one (if possible) will be used .
    lib = 'talib'

    @classmethod
    def calculate_indicator(cls, indicator, data, *args, **kwargs):

        indicator = str(indicator).upper()
        fn = None
        for k, v in _groups_functions.items():
            if indicator in v:
                mod = importlib.import_module(k)
                fn = getattr(mod, indicator)

        return fn(data, *args, **kwargs)

    @classmethod
    def get_groups(cls):
        """
        Just return groups names

        :return: groups names
        """

        return sorted([k for k in _groups_functions.keys()])

    @classmethod
    def get_functions(cls):
        """
        Return all functions supported by this lib

        :return: all functions supported by this lib
        """
        return sorted(_function_list)
