# -*- coding:utf-8 -*-


class Experimental:

    def SAVGP(cls, data):
        """
        Swing Average Price - previous Average Price
        """
        savgp_list = []
        avgp_list = jhta.AVGPRICE(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                savgp = float('NaN')
            else:
                savgp = avgp_list[i] - avgp_list[i - 1]
            savgp_list.append(savgp)
            i += 1
        return savgp_list


    def SAVGPS(cls, data):
        """
        Swing Average Price - previous Average Price Summation
        """
        savgps_list = []
        savgp_list = cls.SAVGP(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                savgps = float('NaN')
                savgps_list.append(savgps)
                savgps = .0
            else:
                savgps = savgps + savgp_list[i]
                savgps_list.append(savgps)
            i += 1
        return savgps_list


    def SCO(cls, data):
        """
        Swing Close - Open
        """
        sco_list = []
        i = 0
        while i < len(data['close']):
            sco = data['close'][i] - data['open'][i]
            sco_list.append(sco)
            i += 1
        return sco_list


    def SCOS(cls, data):
        """
        Swing Close - Open Summation
        """
        scos_list = []
        sco_list = cls.SCO(data)
        scos = .0
        i = 0
        while i < len(data['close']):
            scos = scos + sco_list[i]
            scos_list.append(scos)
            i += 1
        return scos_list


    def SMEDP(cls, data):
        """
        Swing Median Price - previous Median Price
        """
        smedp_list = []
        medp_list = jhta.MEDPRICE(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                smedp = float('NaN')
            else:
                smedp = medp_list[i] - medp_list[i - 1]
            smedp_list.append(smedp)
            i += 1
        return smedp_list


    def SMEDPS(cls, data):
        """
        Swing Median Price - previous Median Price Summation
        """
        smedps_list = []
        smedp_list = cls.SMEDP(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                smedps = float('NaN')
                smedps_list.append(smedps)
                smedps = .0
            else:
                smedps = smedps + smedp_list[i]
                smedps_list.append(smedps)
            i += 1
        return smedps_list


    def SPP(cls, df, price='close'):
        """
        Swing Price - previous Price
        """
        spp_list = []
        i = 0
        while i < len(df[price]):
            if i < 1:
                spp = float('NaN')
            else:
                spp = df[price][i] - df[price][i - 1]
            spp_list.append(spp)
            i += 1
        return spp_list


    def SPPS(cls, df, price='close'):
        """
        Swing Price - previous Price Summation
        """
        spps_list = []
        spp_list = cls.SPP(df, price)
        i = 0
        while i < len(df[price]):
            if i < 1:
                spps = float('NaN')
                spps_list.append(spps)
                spps = .0
            else:
                spps = spps + spp_list[i]
                spps_list.append(spps)
            i += 1
        return spps_list


    def STYPP(cls, data):
        """
        Swing Typical Price - previous Typical Price
        """
        stypp_list = []
        typp_list = jhta.TYPPRICE(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                stypp = float('NaN')
            else:
                stypp = typp_list[i] - typp_list[i - 1]
            stypp_list.append(stypp)
            i += 1
        return stypp_list


    def STYPPS(cls, data):
        """
        Swing Typical Price - previous Typical Price Summation
        """
        stypps_list = []
        stypp_list = cls.STYPP(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                stypps = float('NaN')
                stypps_list.append(stypps)
                stypps = .0
            else:
                stypps = stypps + stypp_list[i]
                stypps_list.append(stypps)
            i += 1
        return stypps_list


    def SWCLP(cls, data):
        """
        Swing Weighted Close Price - previous Weighted Close Price
        """
        swclp_list = []
        wclp_list = jhta.WCLPRICE(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                swclp = float('NaN')
            else:
                swclp = wclp_list[i] - wclp_list[i - 1]
            swclp_list.append(swclp)
            i += 1
        return swclp_list


    def SWCLPS(cls, data):
        """
        Swing Weighted Close Price - previous Weighted Close Price Summation
        """
        swclps_list = []
        swclp_list = cls.SWCLP(data)
        i = 0
        while i < len(data['close']):
            if i < 1:
                swclps = float('NaN')
                swclps_list.append(swclps)
                swclps = .0
            else:
                swclps = swclps + swclp_list[i]
                swclps_list.append(swclps)
            i += 1
        return swclps_list
