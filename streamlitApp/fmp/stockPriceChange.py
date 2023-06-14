from .__model import Model

class StockPriceChange(Model):
    def __init__(self):
        self.symbol = None
        self.V1D = None
        self.V5D = None
        self.V1M = None
        self.V3M = None
        self.V6M = None
        self.Vytd = None
        self.V1Y = None
        self.V3Y = None
        self.V5Y = None
        self.V10Y = None
        self.Vmax = None

        self.response = None

    def from_dict(self,json_params):
        self.symbol = json_params['symbol']
        self.V1D = json_params['1D']
        self.V5D = json_params['5D']
        self.V1M = json_params['1M']
        self.V3M = json_params['3M']
        self.V6M = json_params['6M']
        self.Vytd = json_params['ytd']
        self.V1Y = json_params['1Y']
        self.V3Y = json_params['3Y']
        self.V5Y = json_params['5Y']
        self.v10Y = json_params['10Y']
        self.Vmax = json_params['max']


