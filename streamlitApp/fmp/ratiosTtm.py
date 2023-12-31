from .__model import Model

class RatiosTTM(Model):
    def __init__(self):
        self.dividendYielTTM = None
        self.dividendYielPercentageTTM = None
        self.peRatioTTM = None
        self.pegRatioTTM = None
        self.payoutRatioTTM = None
        self.currentRatioTTM = None
        self.quickRatioTTM = None
        self.cashRatioTTM = None
        self.daysOfSalesOutstandingTTM = None
        self.daysOfInventoryOutstandingTTM = None
        self.operatingCycleTTM = None
        self.daysOfPayablesOutstandingTTM = None
        self.cashConversionCycleTTM = None
        self.grossProfitMarginTTM = None
        self.operatingProfitMarginTTM = None
        self.pretaxProfitMarginTTM = None
        self.netProfitMarginTTM = None
        self.effectiveTaxRateTTM = None
        self.returnOnAssetsTTM = None
        self.returnOnEquityTTM = None
        self.returnOnCapitalEmployedTTM = None
        self.netIncomePerEBTTTM = None
        self.ebtPerEbitTTM = None
        self.ebitPerRevenueTTM = None
        self.debtRatioTTM = None
        self.debtEquityRatioTTM = None
        self.longTermDebtToCapitalizationTTM = None
        self.totalDebtToCapitalizationTTM = None
        self.interestCoverageTTM = None
        self.cashFlowToDebtRatioTTM = None
        self.companyEquityMultiplierTTM = None
        self.receivablesTurnoverTTM = None
        self.payablesTurnoverTTM = None
        self.inventoryTurnoverTTM = None
        self.fixedAssetTurnoverTTM = None
        self.assetTurnoverTTM = None
        self.operatingCashFlowPerShareTTM = None
        self.freeCashFlowPerShareTTM = None
        self.cashPerShareTTM = None
        self.operatingCashFlowSalesRatioTTM = None
        self.freeCashFlowOperatingCashFlowRatioTTM = None
        self.cashFlowCoverageRatiosTTM = None
        self.shortTermCoverageRatiosTTM = None
        self.capitalExpenditureCoverageRatioTTM = None
        self.dividendPaidAndCapexCoverageRatioTTM = None
        self.priceBookValueRatioTTM = None
        self.priceToBookRatioTTM = None
        self.priceToSalesRatioTTM = None
        self.priceEarningsRatioTTM = None
        self.priceToFreeCashFlowsRatioTTM = None
        self.priceToOperatingCashFlowsRatioTTM = None
        self.priceCashFlowRatioTTM = None
        self.priceEarningsToGrowthRatioTTM = None
        self.priceSalesRatioTTM = None
        self.dividendYieldTTM = None
        self.enterpriseValueMultipleTTM = None
        self.priceFairValueTTM = None
        self.dividendPerShareTTM = None

        self.response = None

    def from_dict(self,json_params):
        self.dividendYielTTM = json_params['dividendYielTTM']
        self.dividendYielPercentageTTM = json_params['dividendYielPercentageTTM']
        self.peRatioTTM = json_params['peRatioTTM']
        self.pegRatioTTM = json_params['pegRatioTTM']
        self.payoutRatioTTM = json_params['payoutRatioTTM']
        self.currentRatioTTM = json_params['currentRatioTTM']
        self.quickRatioTTM = json_params['quickRatioTTM']
        self.cashRatioTTM = json_params['cashRatioTTM']
        self.daysOfSalesOutstandingTTM = json_params['daysOfSalesOutstandingTTM']
        self.daysOfInventoryOutstandingTTM = json_params['daysOfInventoryOutstandingTTM']
        self.operatingCycleTTM = json_params['operatingCycleTTM']
        self.daysOfPayablesOutstandingTTM = json_params['daysOfPayablesOutstandingTTM']
        self.cashConversionCycleTTM = json_params['cashConversionCycleTTM']
        self.grossProfitMarginTTM = json_params['grossProfitMarginTTM']
        self.operatingProfitMarginTTM = json_params['operatingProfitMarginTTM']
        self.pretaxProfitMarginTTM = json_params['pretaxProfitMarginTTM']
        self.netProfitMarginTTM = json_params['netProfitMarginTTM']
        self.effectiveTaxRateTTM = json_params['effectiveTaxRateTTM']
        self.returnOnAssetsTTM = json_params['returnOnAssetsTTM']
        self.returnOnEquityTTM = json_params['returnOnEquityTTM']
        self.returnOnCapitalEmployedTTM = json_params['returnOnCapitalEmployedTTM']
        self.netIncomePerEBTTTM = json_params['netIncomePerEBTTTM']
        self.ebtPerEbitTTM = json_params['ebtPerEbitTTM']
        self.ebitPerRevenueTTM = json_params['ebitPerRevenueTTM']
        self.debtRatioTTM = json_params['debtRatioTTM']
        self.debtEquityRatioTTM = json_params['debtEquityRatioTTM']
        self.longTermDebtToCapitalizationTTM = json_params['longTermDebtToCapitalizationTTM']
        self.totalDebtToCapitalizationTTM = json_params['totalDebtToCapitalizationTTM']
        self.interestCoverageTTM = json_params['interestCoverageTTM']
        self.cashFlowToDebtRatioTTM = json_params['cashFlowToDebtRatioTTM']
        self.companyEquityMultiplierTTM = json_params['companyEquityMultiplierTTM']
        self.receivablesTurnoverTTM = json_params['receivablesTurnoverTTM']
        self.payablesTurnoverTTM = json_params['payablesTurnoverTTM']
        self.inventoryTurnoverTTM = json_params['inventoryTurnoverTTM']
        self.fixedAssetTurnoverTTM = json_params['fixedAssetTurnoverTTM']
        self.assetTurnoverTTM = json_params['assetTurnoverTTM']
        self.operatingCashFlowPerShareTTM = json_params['operatingCashFlowPerShareTTM']
        self.freeCashFlowPerShareTTM = json_params['freeCashFlowPerShareTTM']
        self.cashPerShareTTM = json_params['cashPerShareTTM']
        self.operatingCashFlowSalesRatioTTM = json_params['operatingCashFlowSalesRatioTTM']
        self.freeCashFlowOperatingCashFlowRatioTTM = json_params['freeCashFlowOperatingCashFlowRatioTTM']
        self.cashFlowCoverageRatiosTTM = json_params['cashFlowCoverageRatiosTTM']
        self.shortTermCoverageRatiosTTM = json_params['shortTermCoverageRatiosTTM']
        self.capitalExpenditureCoverageRatioTTM = json_params['capitalExpenditureCoverageRatioTTM']
        self.dividendPaidAndCapexCoverageRatioTTM = json_params['dividendPaidAndCapexCoverageRatioTTM']
        self.priceBookValueRatioTTM = json_params['priceBookValueRatioTTM']
        self.priceToBookRatioTTM = json_params['priceToBookRatioTTM']
        self.priceToSalesRatioTTM = json_params['priceToSalesRatioTTM']
        self.priceEarningsRatioTTM = json_params['priceEarningsRatioTTM']
        self.priceToFreeCashFlowsRatioTTM = json_params['priceToFreeCashFlowsRatioTTM']
        self.priceToOperatingCashFlowsRatioTTM = json_params['priceToOperatingCashFlowsRatioTTM']
        self.priceCashFlowRatioTTM = json_params['priceCashFlowRatioTTM']
        self.priceEarningsToGrowthRatioTTM = json_params['priceEarningsToGrowthRatioTTM']
        self.priceSalesRatioTTM = json_params['priceSalesRatioTTM']
        self.dividendYieldTTM = json_params['dividendYieldTTM']
        self.enterpriseValueMultipleTTM = json_params['enterpriseValueMultipleTTM']
        self.priceFairValueTTM = json_params['priceFairValueTTM']
        self.dividendPerShareTTM = json_params['dividendPerShareTTM']


class RatiosTTM_List(Model):
    def __init__(self):
        self.values = []
        self.response = None