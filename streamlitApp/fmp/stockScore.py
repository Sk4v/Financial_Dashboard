from .__model import Model

class StockFinancialScore(Model):
    def __init__(self):
        self.symbol = None
        self.altmanZScore = None
        self.piotroskiScore = None
        self.workingCapital = None
        self.totalAssets = None
        self.retainedEarnings = None
        self.ebit = None
        self.marketCap = None
        self.totalLiabilities = None
        self.revenue = None

        self.response = None

    def from_dict(self,json_params):
        self.symbol = json_params['symbol']
        self.altmanZScore = json_params['altmanZScore']
        self.piotroskiScore = json_params['piotroskiScore']
        self.workingCapital = json_params['workingCapital']
        self.totalAssets = json_params['totalAssets']
        self.retainedEarnings = json_params['retainedEarnings']
        self.ebit = json_params['ebit']
        self.marketCap = json_params['marketCap']
        self.totalLiabilities = json_params['totalLiabilities']
        self.revenue = json_params['revenue']



