# -*- coding:utf-8 -*-
from cycle import WCLPRICE
from prices import TYPPRICE, AVGPRICE, MEDPRICE

__all__ = ['SAVGP', 'SAVGPS', 'SCO', 'SCOS', 'SMEDP', 'SMEDPS', 'SPP', 'SPPS', 'STYPP', 'STYPPS', 'SWCLP', 'SWCLPS']


def SAVGP(data):
    """
    Swing Average Price
    
    Previous Average Price.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    savgp_list = []
    average_price_list = AVGPRICE(data)
    i = 0
    while i < len(data['close']):
        if i < 1:
            savgp = float('NaN')
        else:
            savgp = average_price_list[i] - average_price_list[i - 1]
        savgp_list.append(savgp)
        i += 1
    return savgp_list


def SAVGPS(data):
    """
    Swing Average Price
    
    Previous Average Price Summation.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    savgps_list = []
    savgp_list = SAVGP(data)
    i = 0
    savgps = .0
    while i < len(data['close']):
        if i < 1:
            savgps = float('NaN')
            savgps_list.append(savgps)
            savgps = .0
        else:
            savgps += savgp_list[i]
            savgps_list.append(savgps)
        i += 1
    return savgps_list


def SCO(data):
    """
    Swing Close
    
    Open.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    sco_list = []
    i = 0
    while i < len(data['close']):
        sco = data['close'][i] - data['open'][i]
        sco_list.append(sco)
        i += 1
    return sco_list


def SCOS(data):
    """
    Swing Close
     
    Open Summation.
     
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    scos_list = []
    sco_list = SCO(data)
    scos = .0
    i = 0
    while i < len(data['close']):
        scos = scos + sco_list[i]
        scos_list.append(scos)
        i += 1
    return scos_list


def SMEDP(data):
    """
    Swing Median Price
    
    Previous Median Price.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """

    smedp_list = []
    median_price = MEDPRICE(data)
    i = 0
    while i < len(data['close']):
        if i < 1:
            smedp = float('NaN')
        else:
            smedp = median_price[i] - median_price[i - 1]
        smedp_list.append(smedp)
        i += 1
    return smedp_list


def SMEDPS(data):
    """
    Swing Median Price
    
    Previous Median Price Summation.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    smedps_list = []
    smedp_list = SMEDP(data)
    i = 0
    smedps = .0
    while i < len(data['close']):
        if i < 1:
            smedps = float('NaN')
            smedps_list.append(smedps)
            smedps = .0
        else:
            smedps += smedp_list[i]
            smedps_list.append(smedps)
        i += 1
    return smedps_list


def SPP(data, price='close'):
    """
    Swing Price
    
    Previous Price
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param str price: 
    :return pd.Series: with indicator data calculation results
    """
    spp_list = []
    i = 0
    while i < len(data[price]):
        if i < 1:
            spp = float('NaN')
        else:
            spp = data[price][i] - data[price][i - 1]
        spp_list.append(spp)
        i += 1
    return spp_list


def SPPS(data, price='close'):
    """
    Swing Price
    
    Previous Price Summation.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    spps_list = []
    spp_list = SPP(data, price)
    i = 0
    spps = .0
    while i < len(data[price]):
        if i < 1:
            spps = float('NaN')
            spps_list.append(spps)
            spps = .0
        else:
            spps += spp_list[i]
            spps_list.append(spps)
        i += 1
    return spps_list


def STYPP(data):
    """
    Swing Typical Price 
    
    Previous Typical Price
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    stypp_list = []
    typical_price = TYPPRICE(data)
    i = 0
    while i < len(data['close']):
        if i < 1:
            stypp = float('NaN')
        else:
            stypp = typical_price[i] - typical_price[i - 1]
        stypp_list.append(stypp)
        i += 1
    return stypp_list


def STYPPS(data):
    """
    Swing Typical Price
    
    Previous Typical Price Summation.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    stypps_list = []
    stypp_list = STYPP(data)
    i = 0
    stypps = .0
    while i < len(data['close']):
        if i < 1:
            stypps = float('NaN')
            stypps_list.append(stypps)
            stypps = .0
        else:
            stypps += stypp_list[i]
            stypps_list.append(stypps)
        i += 1
    return stypps_list


def SWCLP(data):
    """
    Swing Weighted Close Price
    
    Previous Weighted Close Price
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    swclp_list = []
    weighted_close_price = WCLPRICE(data)
    i = 0
    while i < len(data['close']):
        if i < 1:
            swclp = float('NaN')
        else:
            swclp = weighted_close_price[i] - weighted_close_price[i - 1]
        swclp_list.append(swclp)
        i += 1
    return swclp_list


def SWCLPS(data):
    """
    Swing Weighted Close Price
    
    Previous Weighted Close Price Summation.
    
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    swclps_list = []
    swclp_list = SWCLP(data)
    i = 0
    swclps = .0
    while i < len(data['close']):
        if i < 1:
            swclps = float('NaN')
            swclps_list.append(swclps)
            swclps = .0
        else:
            swclps += swclp_list[i]
            swclps_list.append(swclps)
        i += 1
    return swclps_list
