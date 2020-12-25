def aggregate_bar(self, data):
    """
    Aggregate with the arrival of new trades data
    :param data : A data object containing the ticks of a
    single timestamp or tick.
    """
    self.cum_count['cum_tick'] += 1
    self.cum_count['cum_volume'] += data.size
    self.cum_count['cum_dollar_value'] += data.price*data.size
    self.price.append(data.price)
    self.volume.append(data.size)
    #check the side of the trade
    tick_sign = self._check_tick_sign(data.price)
    if tick_sign > 0:
        self.cum_count['cum_buy_tick'] += 1
        self.cum_count['cum_buy_volume'] += data.size
        self.cum_count['cum_buy_dollar_value'] += data.price*data.size

    if self.cum_count[self.stat] >= self.threshold:
        #getting the vwap
        vwap = np.multiply(self.price, self.volume).sum()/
                sum(self.volume)
        bar = {'timestamp': str(data.timestamp),
                'symbol' : data.symbol,'open':self.price[0], 
                'high':max(self.price), 'low': min(self.price), 
                'close': data.price, 'vwap' : vwap}
        #join the cumulative metrics to the bar
        bar.update(self.cum_count)
        #save the bar
        self.save_bar(list(bar.values()))
        print(bar)
        self._reset_cache()
        return bar
    return False

def get_tick_bars(symbols:Union[str, list], threshold:Union[int, dict], 
                  save_to:str):
    """
    Get RealTime Tick Bars.

    :param symbols :(str or list) a ticker symbol or a list of ticker 
                    symbols to generate the bars.
    :param threshold :(int or dict) threshold for bar formation or 
                      sampling. A dictionary must be given if bars 
                      to generate for multiple symbols. The dictionary 
                      keys are ticker symbols and values are the 
                      thresholds respectively.
    :param save_to :(str) the path to store the bars.
    :return :(None)
    """
    get_bars('tick_bar', symbols, threshold, save_to)

def get_dollar_bars(symbols:Union[str, list], threshold:Union[int, dict],
                    save_to:str):
        """
        Get RealTime Dollar Bars.

        :param symbols :(str or list) a ticker symbol or a list of ticker
                        symbols to generate the bars.
        :param threshold :(int or dict) threshold for bar formation or
                          sampling. A dictionary must be given if bars
                          to generate for multiple symbols. The dictionary
                          keys are ticker symbols and values are the
                          thresholds respectively.
        :param save_to :(str) the path to store the bars.
        :return :(None)
        """
        get_bars('dollar_bar', symbols, threshold, save_to)
