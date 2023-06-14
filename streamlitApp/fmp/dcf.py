from .__model import Model

class DCF(Model):
    def __init__(self):
        self.symbol = None
        self.date = None
        self.dcf = None
        self.dcf_format = None
        self.stock_price = None

        self.response = None


    def from_dict(self,json_params):
        self.symbol = json_params['symbol']
        self.date = json_params['date']
        self.dcf = json_params['dcf']
        self.dcf_format = "{:.2f}".format(int(json_params['dcf']))
        self.stock_price = json_params['Stock Price']

class AdvancedDCF(Model):
    def __init__(self):
        self.year = None
        self.symbol = None
        self.revenue = None
        self.revenuePercentage = None
        self.ebitda = None
        self.ebitdaPercentage = None
        self.ebit = None
        self.ebitPercentage = None
        self.depreciation = None
        self.depreciationPercentage = None
        self.totalCash = None
        self.totalCashPercentage = None
        self.receivables = None
        self.receivablesPercentage = None
        self.inventories = None
        self.inventoriesPercentage = None
        self.payable = None
        self.payablePercentage = None
        self.capitalExpenditure = None
        self.capitalExpenditurePercentage = None
        self.price = None
        self.beta = None
        self.dilutedSharesOutstanding = None
        self.costofDebt = None
        self.taxRate = None
        self.afterTaxCostOfDebt = None
        self.riskFreeRate = None
        self.marketRiskPremium = None
        self.costOfEquity = None
        self.totalDebt = None
        self.totalEquity = None
        self.totalCapital = None
        self.debtWeighting = None
        self.equityWeighting = None
        self.wacc = None
        self.taxRateCash = None
        self.ebiat = None
        self.ufcf = None
        self.sumPvUfcf = None
        self.longTermGrowthRate = None
        self.terminalValue = None
        self.presentTerminalValue = None
        self.enterpriseValue = None
        self.netDebt = None
        self.equityValue = None
        self.equityValuePerShare = None
        self.freeCashFlowT1 = None

        self.response = None

    def from_dict(self,json_params):
        self.year = json_params['year']
        self.symbol = json_params['symbol']
        self.revenue = json_params['revenue']
        self.revenuePercentage = json_params['revenuePercentage']
        self.ebitda = json_params['ebitda']
        self.ebitdaPercentage = json_params['ebitdaPercentage']
        self.ebit = json_params['ebit']
        self.ebitPercentage = json_params['ebitPercentage']
        self.depreciation = json_params['depreciation']
        self.depreciationPercentage = json_params['depreciationPercentage']
        self.totalCash = json_params['totalCash']
        self.totalCashPercentage = json_params['totalCashPercentage']
        self.receivables = json_params['receivables']
        self.receivablesPercentage = json_params['receivablesPercentage']
        self.inventories = json_params['inventories']
        self.inventoriesPercentage = json_params['inventoriesPercentage']
        self.payable = json_params['payable']
        self.payablePercentage = json_params['payablePercentage']
        self.capitalExpenditure = json_params['capitalExpenditure']
        self.capitalExpenditurePercentage = json_params['capitalExpenditurePercentage']
        self.price = json_params['price']
        self.beta = json_params['beta']
        self.dilutedSharesOutstanding = json_params['dilutedSharesOutstanding']
        self.costofDebt = json_params['costofDebt']
        self.taxRate = json_params['taxRate']
        self.afterTaxCostOfDebt = json_params['afterTaxCostOfDebt']
        self.riskFreeRate = json_params['riskFreeRate']
        self.marketRiskPremium = json_params['marketRiskPremium']
        self.costOfEquity = json_params['costOfEquity']
        self.totalDebt = json_params['totalDebt']
        self.totalEquity = json_params['totalEquity']
        self.totalCapital = json_params['totalCapital']
        self.debtWeighting = json_params['debtWeighting']
        self.equityWeighting = json_params['equityWeighting']
        self.wacc = json_params['wacc']
        self.taxRateCash = json_params['taxRateCash']
        self.ebiat = json_params['ebiat']
        self.ufcf = json_params['ufcf']
        self.sumPvUfcf = json_params['sumPvUfcf']
        self.longTermGrowthRate = json_params['longTermGrowthRate']
        self.terminalValue = json_params['terminalValue']
        self.presentTerminalValue = json_params['presentTerminalValue']
        self.enterpriseValue = json_params['enterpriseValue']
        self.netDebt = json_params['netDebt']
        self.equityValue = json_params['equityValue']
        self.equityValuePerShare = json_params['equityValuePerShare']
        self.freeCashFlowT1 = json_params['freeCashFlowT1']

class AdvancedDCF_List(Model):
    def __init__(self):
        self.values = []
        self.response = None


class AdvancedLeveredDiscountedCashFlow(Model):
    def __init__(self):
        self.year = None
        self.symbol = None
        self.revenue = None
        self.revenuePercentage = None
        self.capitalExpenditure = None
        self.capitalExpenditurePercentage = None
        self.price = None
        self.beta = None
        self.dilutedSharesOutstanding = None
        self.costofDebt = None
        self.taxRate = None
        self.afterTaxCostOfDebt = None
        self.riskFreeRate = None
        self.marketRiskPremium = None
        self.costOfEquity = None
        self.totalDebt = None
        self.totalEquity = None
        self.totalCapital = None
        self.debtWeighting = None
        self.equityWeighting = None
        self.wacc = None
        self.operatingCashFlow = None
        self.pvLfcf = None
        self.sumPvLfcf = None
        self.longTermGrowthRate = None
        self.freeCashFlow = None
        self.terminalValue = None
        self.presentTerminalValue = None
        self.enterpriseValue = None
        self.netDebt = None
        self.equityValue = None
        self.equityValuePerShare = None
        self.freeCashFlowT1 = None
        self.operatingCashFlowPercentage = None

        self.response = None

    def from_dict(self,json_params):
        self.year = json_params['year']
        self.symbol = json_params['symbol']
        self.revenue = json_params['revenue']
        self.revenuePercentage = json_params['revenuePercentage']
        self.capitalExpenditure = json_params['capitalExpenditure']
        self.capitalExpenditurePercentage = json_params['capitalExpenditurePercentage']
        self.price = json_params['price']
        self.beta = json_params['beta']
        self.dilutedSharesOutstanding = json_params['dilutedSharesOutstanding']
        self.costofDebt = json_params['costofDebt']
        self.taxRate = json_params['taxRate']
        self.afterTaxCostOfDebt = json_params['afterTaxCostOfDebt']
        self.riskFreeRate = json_params['riskFreeRate']
        self.marketRiskPremium = json_params['marketRiskPremium']
        self.costOfEquity = json_params['costOfEquity']
        self.totalDebt = json_params['totalDebt']
        self.totalEquity = json_params['totalEquity']
        self.totalCapital = json_params['totalCapital']
        self.debtWeighting = json_params['debtWeighting']
        self.equityWeighting = json_params['equityWeighting']
        self.wacc = json_params['wacc']
        self.operatingCashFlow = json_params['operatingCashFlow']
        self.pvLfcf = json_params['pvLfcf']
        self.sumPvLfcf = json_params['sumPvLfcf']
        self.longTermGrowthRate = json_params['longTermGrowthRate']
        self.freeCashFlow = json_params['freeCashFlow']
        self.terminalValue = json_params['terminalValue']
        self.presentTerminalValue = json_params['presentTerminalValue']
        self.enterpriseValue = json_params['enterpriseValue']
        self.netDebt = json_params['netDebt']
        self.equityValue = json_params['equityValue']
        self.equityValuePerShare = json_params['equityValuePerShare']
        self.freeCashFlowT1 = json_params['freeCashFlowT1']
        self.operatingCashFlowPercentage = json_params['operatingCashFlowPercentage']


