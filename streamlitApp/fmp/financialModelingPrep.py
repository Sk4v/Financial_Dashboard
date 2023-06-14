import requests
import sys
from pathlib import Path

path = Path(__file__).parent
#path = os.path.join(path,'.env')
print('path: ',path)
sys.path.append(path)

from .responseModel import ResponseModel
from .ratiosTtm import RatiosTTM
from .keyMetrics import KeyMetricsTTM
from .stockScore import StockFinancialScore
from .companyProfile import CompanyProfile
from .dcf import DCF, AdvancedDCF_List
from .historycal_dcf import HistoricalDCF
from .stockPriceChange import StockPriceChange
from .historical_price import HistoricalPriceList
from .stockPeers import StockPeers


class FinancialModelingPrep():
    def __init__(self, token):
        self.url_api = "https://financialmodelingprep.com/"
        self.token = token

    @staticmethod
    def detect_name(key):
        '''
        Detect the camel case and create the name variable
        es. dividendYielTTM = Dividend Yiel TTM
        '''
        key_remastered = ''
        ttm = ''
        if key[-3:] == 'TTM':
            ttm = 'TTM'
            key_remastered = key[:-3]
        print(key_remastered)

        if key_remastered != '':
            key = key_remastered
        else:
            pass

        name = ''
        for i in range(len(key)):
            if i == 0:
                name += key[i].upper()
            else:
                if key[i].isupper():
                    name += ' '
                name += key[i]
        return name + ' ' + ttm

    def company_ratios(self, symbol, limit: int = None, quarter=False):
        if quarter:
            if limit:
                url = f'{self.url_api}api/v3/ratios/{symbol}?period=quarter&limit={limit}&apikey={self.token}'
            else:
                url = f'{self.url_api}api/v3/ratios/{symbol}?period=quarter&apikey={self.token}'
        else:
            if limit:
                url = f'{self.url_api}api/v3/ratios/{symbol}?limit={limit}&apikey={self.token}'

            else:
                url = f'{self.url_api}api/v3/ratios/{symbol}?apikey={self.token}'

        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def ratios_ttm(self, symbol):
        url = f'{self.url_api}/api/v3/ratios-ttm/{symbol}?apikey={self.token}'
        response = requests.get(url)
        ratioTTM = RatiosTTM()
        ratioTTM.from_json(response)
        return ratioTTM

    def stock_financial_scores(self, symbol):
        url = f'{self.url_api}api/v4/score?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        stockScore = StockFinancialScore()
        stockScore.from_json(response)
        return stockScore

    def enterprise_values(self, symbol, quarter=False):
        if quarter:
            url = f'{self.url_api}api/v3/enterprise-values/{symbol}?period=quarter&&apikey={self.token}'
        else:
            url = f'{self.url_api}api/v3/enterprise-values/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    # todo varianti con limit e period
    def income_statement_growth(self, symbol):
        url = f'{self.url_api}api/v3/income-statement-growth/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    # Todo varianti con limite
    def balance_sheet_statement_growth(self, symbol):
        url = f'{self.url_api}/api/v3/balance-sheet-statement-growth/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    # Todo varianti con limite
    def cash_flow_statements_growth(self, symbol):
        url = f'{self.url_api}/api/v3/cash-flow-statement-growth/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def cash_flow_statement(self, symbol, limit: int = None, quarter=False):
        '''
        https://site.financialmodelingprep.com/developer/docs/#Company-Financial-Statements
        '''
        if quarter:
            if limit:
                url = f'{self.url_api}/api/v3/cash-flow-statement/{symbol}?period=quarter&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/cash-flow-statement/{symbol}?period=quarter&limit={limit}&apikey={self.token}'
        else:
            if limit:
                url = f'{self.url_api}/api/v3/cash-flow-statement/{symbol}?limit={limit}&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/cash-flow-statement/{symbol}?&apikey={self.token}'

        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def key_metrics_ttm(self, symbol):
        url = f'{self.url_api}/api/v3/key-metrics-ttm/{symbol}?&apikey={self.token}'
        response = requests.get(url)

        keyMetrics_TTM = KeyMetricsTTM()
        keyMetrics_TTM.from_json(response)
        return keyMetrics_TTM

    # Todo varianti con limit
    def key_metrics(self, symbol):
        url = f'{self.url_api}/api/v3/key-metrics/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def company_profile(self, symbol):
        url = f'{self.url_api}/api/v3/profile/{symbol}?apikey={self.token}'
        response = requests.get(url)
        company = CompanyProfile()
        company.from_json(response)
        return company

    # Todo varianti con limit
    def financial_growth(self, symbol):
        url = f'{self.url_api}/api/v3/financial-growth/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def discounted_cash_flow(self, symbol):
        url = f'{self.url_api}/api/v3/discounted-cash-flow/{symbol}?apikey={self.token}'
        print(url)
        response = requests.get(url)
        dcf = DCF()
        dcf.from_json(response)
        return dcf

    def advanced_discounted_cash_flow(self, symbol):
        url = f'{self.url_api}/api/v4/advanced_discounted_cash_flow?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        adv_dcf = AdvancedDCF_List()
        adv_dcf.from_json_list(adv_dcf.values, response)
        return adv_dcf

    # Todo test
    def advanced_levered_discounted_cash_flow(self, symbol):
        url = f'{self.url_api}/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    # Todo test
    def __historical_dfc(self, url):
        response = requests.get(url)
        historical = HistoricalDCF()
        historical.from_json(response)
        return historical

    def historical_discounted_cash_flow(self, symbol, limit: int = None):
        if limit:
            url = f'{self.url_api}/api/v3/historical-discounted-cash-flow-statement/{symbol}?&limit={limit}&apikey={self.token}'
        else:
            url = f'{self.url_api}/api/v3/historical-discounted-cash-flow-statement/{symbol}?apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    # Todo test
    def historical_daily_discounted_cash_flow(self, symbol):
        url = f'{self.symbol}/v3/historical-daily-discounted-cash-flow/{symbol}?apikey={self.token}'
        historical = self.__historical_dfc(url)
        return historical

    # Todo inserire metodi con limit e periodi
    def historical_rating(self, symbol):
        url = f'{self.url_api}/api/v3/historical-rating/{symbol}?&apikey={self.token}'
        response = requests.get(url)
        print(response.json())
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def stock_news(self, symbol, limit: int = None):
        if limit:
            url = f'{self.url_api}/api/v3/stock_news?tickers={symbol}&limit={limit}&apikey={self.token}'
        else:
            url = f'{self.url_api}/api/v3/stock_news?tickers={symbol}&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def latest_stock_news(self, limit: int = None):
        if limit:
            url = f'{self.url_api}/api/v3/stock_news?limit={limit}&apikey={self.token}'
        else:
            url = f'{self.url_api}/api/v3/stock_news?&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def historical_price_full(self, symbol):
        url = f'{self.url_api}/api/v3/historical-price-full/{symbol}?apikey={self.token}'
        response = requests.get(url)

        historical_price = HistoricalPriceList()
        historical_price.from_json_list(historical_price.historical_values, response)
        historical_price.response = response
        return historical_price

    def stock_price_change(self, symbol):
        url = f'{self.url_api}/api/v3/stock-price-change/{symbol}?apikey={self.token}'
        response = requests.get(url)
        stockPriceChange = StockPriceChange()
        stockPriceChange.from_json(response)
        return stockPriceChange

    def stock_peers(self, symbol):
        url = f'{self.url_api}/api/v4/stock_peers?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        stockPeers = StockPeers()
        stockPeers.from_json(response)
        return stockPeers

    def income_statement(self, symbol, limit: int = None, quarter=False):
        '''
        https://site.financialmodelingprep.com/developer/docs/#Company-Financial-Statements
        '''
        if limit:
            if quarter:
                url = f'{self.url_api}/api/v3/income-statement/{symbol}?period=quarter&limit={limit}&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/income-statement/{symbol}?limit={limit}&apikey={self.token}'
        else:
            if quarter:
                url = f'{self.url_api}/api/v3/income-statement/{symbol}?period=quarter&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/income-statement/{symbol}?&apikey={self.token}'

        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def balance_sheet_statement(self, symbol, limit: int = None, quarter=False):
        '''
        https://site.financialmodelingprep.com/developer/docs/#Company-Financial-Statements
        '''
        if limit:
            if quarter:
                url = f'{self.url_api}/api/v3/balance-sheet-statement/{symbol}?period=quarter&limit={limit}&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/balance-sheet-statement/{symbol}?limit={limit}&apikey={self.token}'
        else:
            if quarter:
                url = f'{self.url_api}/api/v3/balance-sheet-statement/{symbol}?period=quarter&apikey={self.token}'
            else:
                url = f'{self.url_api}/api/v3/balance-sheet-statement/{symbol}?&apikey={self.token}'

        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def majors_indexes(self):
        url = f'{self.url_api}/api/v3/quotes/index?apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def key_executives(self, symbol):
        url = f'{self.url_api}/api/v3/key-executives/{symbol}?apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def revenue_geographic_segmentation(self, symbol, period=False):
        if period:
            url = f'{self.url_api}/api/v4/revenue-geographic-segmentation?symbol={symbol}&period=quarter&structure=flat&apikey={self.token}'
            response = requests.get(url)
            model = ResponseModel()
            model.from_json_list(model.values, response)
            model.response = response
            return model

        else:
            url = f'{self.url_api}/api/v4/revenue-geographic-segmentation?symbol={symbol}&structure=flat&apikey={self.token}'
            response = requests.get(url)
            model = ResponseModel()
            model.from_json_list(model.values, response)
            model.response = response
            return model

    def earning_call_transcript(self, symbol):
        url = f'{self.url_api}/api/v4/earning_call_transcript?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def batch_earning_call_transcript(self, symbol, year):
        url = f'{self.url_api}/api/v4/batch_earning_call_transcript/{symbol}?year={year}&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def financial_reports_dates(self, symbol, year=None):
        url = f'{self.url_api}/api/v4/financial-reports-dates?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def sec_filings(self, symbol, type):
        url = f'{self.url_api}/api/v3/sec_filings/{symbol}?type={type.upper()}&page=0&apikey={self.token}'
        response = requests.get(url)
        model = ResponseModel()
        model.from_json_list(model.values, response)
        model.response = response
        return model

    def company_outlook(self, symbol):
        url = f'{self.url_api}/api/v4/company-outlook?symbol={symbol}&apikey={self.token}'
        response = requests.get(url)
        return response
