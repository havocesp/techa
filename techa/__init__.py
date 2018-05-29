# -*- coding: utf-8 -*-
"""
Python Technical Analysis library
"""
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from techa.core import TaLib

__author__ = 'Daniel J. Umpierrez'
__version__ = '0.1.1'
__package__ = 'techa'
__license__ = 'MIT'
__dependencies__ = ['pandas']

__all__ = ['ASI', 'SI', 'TaLib']


def ASI(data, l):
    """
    Accumulation Swing Index (J. Welles Wilder)
    source: book: New Concepts in Technical Trading Systems
    """
    asi_list = []
    si_list = SI(data, l)
    i = 0
    asi = .0
    while i < len(data['close']):
        if i < 1:
            asi = float('NaN')
            asi_list.append(asi)
            asi = .0
        else:
            asi += si_list[i]
            asi_list.append(asi)
        i += 1
    return asi_list


def SI(data, l):
    """
    Swing Index (J. Welles Wilder)
    From "New Concepts in Technical Trading Systems"

    :param pd.DataFrame data:
    :param l:
    :return:
    """
    si_list = []
    i = 0
    while i < len(data['close']):
        if i < 1:
            si = float('NaN')
        else:
            n = (data['close'][i] - data['close'][i - 1]) + (.5 * (data['close'][i] - data['open'][i])) + (
                    .25 * (data['close'][i - 1] - data['open'][i - 1]))
            r1 = data['high'][i] - data['close'][i - 1]
            r2 = data['low'][i] - data['close'][i - 1]
            r3 = data['high'][i] - data['low'][i]
            if r1 > r2 and r1 > r3:
                r = (data['high'][i] - data['close'][i - 1]) - (.5 * (data['low'][i] - data['close'][i - 1])) + (
                        .25 * (data['close'][i - 1] - data['open'][i - 1]))
            if r2 > r1 and r2 > r3:
                r = (data['low'][i] - data['close'][i - 1]) - (.5 * (data['high'][i] - data['close'][i - 1])) + (
                        .25 * (data['close'][i - 1] - data['open'][i - 1]))
            if r3 > r1 and r3 > r2:
                r = (data['high'][i] - data['low'][i]) + (.25 * (data['close'][i - 1] - data['open'][i - 1]))
            k1 = data['high'][i] - data['close'][i - 1]
            k2 = data['low'][i] - data['close'][i - 1]
            if k1 > k2:
                k = k1
            else:
                k = k2
            si = 50 * (n / r) * (k / l)
        si_list.append(si)
        i += 1
    return si_list
