# -*- coding:utf-8 -*-

class Transform:

    @classmethod
    def AVGPRICE(cls, data):
        """
        Average Price
        source: http://www.fmlabs.com/reference/default.htm?url=AvgPrices.htm
        """
        avgprice_list = []
        i = 0
        while i < len(data['close']):
            avgprice = (data['open'][i] + data['high'][i] + data['low'][i] + data['close'][i]) / 4
            avgprice_list.append(avgprice)
            i += 1
        return avgprice_list


    @classmethod
    def MEDPRICE(cls, data):
        """
        Median Price
        source: http://www.fmlabs.com/reference/default.htm?url=MedianPrices.htm
        """
        medprice_list = []
        i = 0
        while i < len(data['close']):
            medprice = (data['high'][i] + data['low'][i]) / 2
            medprice_list.append(medprice)
            i += 1
        return medprice_list


    @classmethod
    def TYPPRICE(cls, data):
        """
        Typical Price
        source: http://www.fmlabs.com/reference/default.htm?url=TypicalPrices.htm
        """
        typprice_list = []
        i = 0
        while i < len(data['close']):
            typprice = (data['high'][i] + data['low'][i] + data['close'][i]) / 3
            typprice_list.append(typprice)
            i += 1
        return typprice_list


    @classmethod
    def WCLPRICE(cls, data):
        """
        Weighted Close Price
        source: http://www.fmlabs.com/reference/default.htm?url=WeightedCloses.htm
        """
        wclprice_list = []
        i = 0
        while i < len(data['close']):
            wclprice = (data['high'][i] + data['low'][i] + (data['close'][i] * 2)) / 4
            wclprice_list.append(wclprice)
            i += 1
        return wclprice_list
