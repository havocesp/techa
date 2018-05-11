"""
Pattern Recognition
"""
from talib.abstract import Function


class Pattern:
    """
    Pattern Recognition
    """


    @classmethod
    def CDL2CROWS(cls, data):
        """
        Two Crows

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL2CROWS')
        return fn(data)


    @classmethod
    def CDL3BLACKCROWS(cls, data):
        """
        Three Black Crows

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3BLACKCROWS')
        return fn(data)


    @classmethod
    def CDL3INSIDE(cls, data):
        """
        Three Inside Up/Down

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3INSIDE')
        return fn(data)


    @classmethod
    def CDL3LINESTRIKE(cls, data):
        """
        Three-Line Strike

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3LINESTRIKE')
        return fn(data)


    @classmethod
    def CDL3OUTSIDE(cls, data):
        """
        Three Outside Up/Down

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3OUTSIDE')
        return fn(data)


    @classmethod
    def CDL3STARSINSOUTH(cls, data):
        """
        Three Stars In The South
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3STARSINSOUTH')
        return fn(data)


    @classmethod
    def CDL3WHITESOLDIERS(cls, data):
        """
        Three Advancing White Soldiers

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDL3WHITESOLDIERS')
        return fn(data)


    @classmethod
    def CDLABANDONEDBABY(cls, data):
        """
        Abandoned Baby
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLABANDONEDBABY')
        return fn(data)


    @classmethod
    def CDLADVANCEBLOCK(cls, data):
        """
        Advance Block

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLADVANCEBLOCK')
        return fn(data)


    @classmethod
    def CDLBELTHOLD(cls, data):
        """
        Belt-hold

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLBELTHOLD')
        return fn(data)


    @classmethod
    def CDLBREAKAWAY(cls, data):
        """
        Breakaway

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLBREAKAWAY')
        return fn(data)


    @classmethod
    def CDLCLOSINGMARUBOZU(cls, data):
        """
        Closing Marubozu

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLCLOSINGMARUBOZU')
        return fn(data)


    @classmethod
    def CDLCONCEALBABYSWALL(cls, data):
        """
        Concealing Baby Swallow

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLCONCEALBABYSWALL')
        return fn(data)


    @classmethod
    def CDLCOUNTERATTACK(cls, data):
        """
        Counterattack

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLCOUNTERATTACK')
        return fn(data)


    @classmethod
    def CDLDARKCLOUDCOVER(cls, data):
        """
        Dark Cloud Cover

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLDARKCLOUDCOVER')
        return fn(data)


    @classmethod
    def CDLDOJI(cls, data):
        """
        Doji

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLDOJI')
        return fn(data)


    @classmethod
    def CDLDOJISTAR(cls, data):
        """
        Doji Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLDOJISTAR')
        return fn(data)


    @classmethod
    def CDLDRAGONFLYDOJI(cls, data):
        """
        Dragon Fly Doji

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLDRAGONFLYDOJI')
        return fn(data)


    @classmethod
    def CDLENGULFING(cls, data):
        """
        Engulfing Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLENGULFING')
        return fn(data)


    @classmethod
    def CDLEVENINGDOJISTAR(cls, data):
        """
        Evening Doji Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLEVENINGDOJISTRAR')
        return fn(data)


    @classmethod
    def CDLEVENINGSTAR(cls, data):
        """
        Evening Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLEVENINGSTAR')
        return fn(data)


    @classmethod
    def CDLGAPSIDESIDEWHITE(cls, data):
        """
        Gap Side

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLGAPSIDESIDEWHITEITE')
        return fn(data)


    @classmethod
    def CDLGRAVESTONEDOJI(cls, data):
        """
        Gravestone Doji

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLGRAVESTONEDOJII')
        return fn(data)


    @classmethod
    def CDLHAMMER(cls, data):
        """
        Hammer

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHAMMER')
        return fn(data)


    @classmethod
    def CDLHANGINGMAN(cls, data):
        """
        Hanging Man

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHANGINGMAN')
        return fn(data)


    @classmethod
    def CDLHARAMI(cls, data):
        """
        Harami Patter

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHARAMI')
        return fn(data)


    @classmethod
    def CDLHARAMICROSS(cls, data):
        """
        Harami Cross Patter

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHARAMICROSS')
        return fn(data)


    @classmethod
    def CDLHIGHWAVE(cls, data):
        """
        High Wave Candle

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHIGHWAVE')
        return fn(data)


    @classmethod
    def CDLHIKKAKE(cls, data):
        """
        Hikkake Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHIKKAKE')
        return fn(data)


    @classmethod
    def CDLHIKKAKEMOD(cls, data):
        """
        Modified Hikkake Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """

        fn = Function('CDLHIKKAKEMOD')
        return fn(data)


    @classmethod
    def CDLHOMINGPIGEON(cls, data):
        """
        Homing Pigeon

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLHOMINGPIGEON')
        return fn(data)


    @classmethod
    def CDLIDENTICAL3CROWS(cls, data):
        """
        Identical 3 Crows

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLIDENTICAL3CROWS')
        return fn(data)


    @classmethod
    def CDLINNECK(cls, data):
        """
        In-Neck Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLINNECK')
        return fn(data)


    @classmethod
    def CDLINVERTEDHAMMER(cls, data):
        """
        Inverted Hammer

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLINVERTEDHAMMER')
        return fn(data)


    @classmethod
    def CDLKICKING(cls, data):
        """
        Kicking

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLKICKING')
        return fn(data)


    @classmethod
    def CDLKICKINGBYLENGTH(cls, data):
        """
        Kicking - bull/bear determined by the longer marubozu

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLKICKINGBYLENGTH')
        return fn(data)


    @classmethod
    def CDLLADDERBOTTOM(cls, data):
        """
        Ladder Bottom

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLLADDERBOTTOM')
        return fn(data)


    @classmethod
    def CDLLONGLEGGEDDOJI(cls, data):
        """
        Long Legged Doji

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLLONGLEGGEDDOJI')
        return fn(data)


    @classmethod
    def CDLLONGLINE(cls, data):
        """
        Long Line Candle

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLLONGLINE')
        return fn(data)


    @classmethod
    def CDLMARUBOZU(cls, data):
        """
        Marubozu

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLMARUBOZU')
        return fn(data)


    @classmethod
    def CDLMATCHINGLOW(cls, data):
        """
        Matching Low

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLMATCHINGLOW')
        return fn(data)


    @classmethod
    def CDLMATHOLD(cls, data):
        """
        Mat Hold

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLMATHOLD')
        return fn(data)


    @classmethod
    def CDLMORNINGDOJISTAR(cls, data):
        """
        Morning Doji Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLMORNINGDOJISTAR')
        return fn(data)


    @classmethod
    def CDLMORNINGSTAR(cls, data):
        """
        Morning Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLMORNINGSTAR')
        return fn(data)


    @classmethod
    def CDLONNECK(cls, data):
        """
        On-Neck Pattern


        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLONNECK')
        return fn(data)


    @classmethod
    def CDLPIERCING(cls, data):
        """
        Piercing Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLPIERCING')
        return fn(data)


    @classmethod
    def CDLRICKSHAWMAN(cls, data):
        """
        Rickshaw Man

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLRICKSHAWMAN')
        return fn(data)


    @classmethod
    def CDLRISEFALL3METHODS(cls, data):
        """
        Rising/Falling Three Methods

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLRISEFALL3METHODS')
        return fn(data)


    @classmethod
    def CDLSEPARATINGLINES(cls, data):
        """
        Separating Lines

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSEPARATINGLINES')
        return fn(data)


    @classmethod
    def CDLSHOOTINGSTAR(cls, data):
        """
        Shooting Star

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSHOOTINGSTAR')
        return fn(data)


    @classmethod
    def CDLSHORTLINE(cls, data):
        """
        Short Line Candle

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSHORTLINE')
        return fn(data)


    @classmethod
    def CDLSPINNINGTOP(cls, data):
        """
        Spinning Top


        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSPINNINGTOP')
        return fn(data)


    @classmethod
    def CDLSTALLEDPATTERN(cls, data):
        """
        Stalled Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSTALLEDPATTERN')
        return fn(data)


    @classmethod
    def CDLSTICKSANDWICH(cls, data):
        """
        Stick Sandwich

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLSTICKSANDWICH')
        return fn(data)


    @classmethod
    def CDLTAKURI(cls, data):
        """
        Takuri (Dragonfly Doji with very long lower shadow)

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLTAKURI')
        return fn(data)


    @classmethod
    def CDLTASUKIGAP(cls, data):
        """
        Tasuki Gap

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLTASUKIGAP')
        return fn(data)


    @classmethod
    def CDLTHRUSTING(cls, data):
        """
        Thrusting Pattern
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLTHRUSTING')
        return fn(data)


    @classmethod
    def CDLTRISTAR(cls, data):
        """
        Tristar Pattern

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLTRISTAR')
        return fn(data)


    @classmethod
    def CDLUNIQUE3RIVER(cls, data):
        """
        Unique 3 River

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLUNIQUE3RIVER')
        return fn(data)


    @classmethod
    def CDLUPSIDEGAP2CROWS(cls, data):
        """


        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLUPSIDEGAP2CROWS')
        return fn(data)


    @classmethod
    def CDLXSIDEGAP3METHODS(cls, data):
        """
        Upside/Downside Gap Three Methods

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CDLXSIDEGAP3METHODS')
        return fn(data)
