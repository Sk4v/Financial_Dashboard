from .__model import Model

class HistoricalPrice(Model):
    def __init__(self):
        self.date = None
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.adjClose = None
        self.volume = None
        self.unadjustedVolume = None
        self.change = None
        self.changePercent = None
        self.vwap = None
        self.label = None
        self.changeOverTime = None

        self.response = None

    def from_dict(self,json_params):
        self.date = json_params['date']
        self.open = json_params['open']
        self.high = json_params['high']
        self.low = json_params['low']
        self.close = json_params['close']
        self.adjClose = json_params['adjClose']
        self.volume = json_params['volume']
        self.unadjustedVolume = json_params['unadjustedVolume']
        self.change = json_params['change']
        self.changePercent = json_params['changePercent']
        self.vwap = json_params['vwap']
        self.label = json_params['label']
        self.changeOverTime = json_params['changeOverTime']

class HistoricalPriceList(Model):
    def __init__(self):
        self.historical_values = []
        self.response = None

    def from_json_list(self,param_list,response):
        json_params = response.json()['historical']
        for element in json_params:
            price = HistoricalPrice()
            price.from_dict(element)
            param_list.append(price)