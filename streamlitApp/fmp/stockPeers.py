from .__model import Model

class StockPeers(Model):
    def __init__(self):
        self.symbol = None
        self.peersList = []
        self. response = None

    def from_dict(self, json_params):
        self.symbol = json_params['symbol']
        self.peersList = json_params['peersList']