# -*- coding:utf-8 -*-
from collections import OrderedDict

from cycle import Cycle
from momentum import Momentum
from overlap import Overlap
from pattern import Pattern
from statistic import Statistic
from volatility import Volatility
from volume import Volume


# noinspection SpellCheckingInspection
class TaLib:
    """
    Technical Analysis Library
    """

    _groups_ref = {
        'Cycle Indicators':      'Cyl',
        'Momentum Indicators':   'Mom',
        'Overlap studies':       'Ovlap',
        'Patter Recognition':    'Pattr',
        'Statistic Functions':   'Stat',
        'Volume Indicators':     'Vol',
        'Volatility Indicators': 'Volat'
    }

    Volat = Volatility
    Olap = Overlap
    Mom = Momentum
    Cycl = Cycle
    Vol = Volume
    Pattr = Pattern
    Stat = Statistic


    @classmethod
    def get_groups(cls):
        """
        Just return groups names

        :return: groups names
        """
        groups = OrderedDict().fromkeys(sorted([grp for grp in cls.__dict__ if grp[0].isupper()]))
        for grp in groups:
            groups.update({grp: [fn for fn in cls.__dict__[grp].__dict__ if fn[0].isupper()]})
        return groups


    @classmethod
    def get_functions(cls):
        """
        Return all functions supported by this lib

        :return: all functions supported by this lib
        """
        result = list()
        for grp in cls.get_groups().values():
            result.extend(grp)
        return sorted(result)


    @classmethod
    def get_function_group(cls, name, display_name=False):
        """
        Get functions grouped by type

        :param str name: function name
        :param bool display_name: if True, full names will be show instead shorted ones
        :return: functions grouped by type
        """
        name = str(name).upper()
        if name in cls.get_functions():
            if name in cls.Pattr.__dict__:
                return cls.Pattr.__name__ if display_name is True else 'Pattr'
            elif name in cls.Mom.__dict__:
                return cls.Mom.__name__ if display_name is True else 'Mom'
            elif name in cls.Olap.__dict__:
                return cls.Olap.__name__ if display_name is True else 'Olap'
            elif name in cls.Vol.__dict__:
                return cls.Vol.__name__ if display_name is True else 'Vol'
            elif name in cls.Cycl.__dict__:
                return cls.Cycl.__name__ if display_name is True else 'Cycl'
            elif name in cls.Stat.__dict__:
                return cls.Stat.__name__ if display_name is True else 'Stat'
            elif name in cls.Volat.__dict__:
                return cls.Volat.__name__ if display_name is True else 'Volat'
