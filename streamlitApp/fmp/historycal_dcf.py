from .__model import Model

class HistoricalDCF(Model):
    def __init__(self):
        self.symbol = None
        self.date = None
        self.dcf = None
        self.stock_price = None

        self.response = None

    def from_dict(self, json_params):
        self.symbol = json_params['symbol']
        self.date = json_params['date']
        self.dcf = json_params['dcf']
        self.stock_price = json_params['Stock Price']