# app.py
from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

data: [(str, [float])] = [
    ("GE", [2.36, 4.15, 4.98, 8.80, 13.51, 21.64, 30.57, 40.51, 42.42, 34.82, 22.25, 31.86]),
    ("MSFT", [2.68, 2.64, 3.68, 5.73, 12.64, 18.49, 43.37, 48.51, 30.26, 31.58, 23.52, 28.16]),
    ("JNJ", [6.78, 7.20, 10.91, 19.43, 24.44, 29.15, 38.04, 39.36, 43.80, 55.19, 52.15, 51.49]),
    ("K", [20.37, 18.47, 19.90, 29.03, 27.59, 38.01, 34.14, 20.93, 23.52, 28.70, 32.00, 37.36]),
    ("BA", [2.34, 4.21, 4.20, 8.09, 13.93, 20.19, 23.47, 36.27, 48.13, 41.39, 32.81, 48.86]),
    ("IBM", [11.79, 14.62, 15.53, 20.41, 30.78, 31.60, 30.94, 39.24, 48.78, 51.05, 59.63, 81.95])
]


class App:

    @staticmethod
    def run():
        # globals
        show = True

        # pm
        stocks: [Stock] = [Stock(item[0], item[1]) for item in data]
        portfolio: [Portfolio] = Portfolio(stocks, show)


class Date:
    def __init__(self):
        pass


# Data represent a nominal percentage of change of a stock based on a specified date.
class Historical:
    date: date
    percentage: float

    def __init__(self, date: date, percentage: float):
        self.date = date
        self.percentage = percentage


class Stock:
    ticker: str
    prices: [float]
    returns: [float]

    def __init__(self, ticker: str, prices: [float]):
        self.ticker = ticker
        self.prices = prices
        self.set_returns(prices)

    def set_returns(self, price):
        returns = self.returns(price)
        average = self.average(returns)
        excess = self.excess(returns, average)
        self.returns = {
            "value": returns,
            "average": average,
            "excess": excess
        }

    def get_returns(self):
        return self.returns["value"]

    """
    This function transform the price data into returns.
    """

    @staticmethod
    def returns(prices: [float]) -> [float]:
        return [np.log(prices[i] / prices[i - 1]) for i in range(1, len(prices))]

    """
    This function implements the calculation for excess returns minus mean.
    """

    @staticmethod
    def excess(returns: [float], average: float) -> [float]:
        return [returns[i] - average for i in range(len(returns))]

    """
    This function implements the average return value over an array of returns.
    """

    @staticmethod
    def average(values: [float]) -> float:
        return np.average(values)

    def __str__(self):
        return self.ticker


class Portfolio:
    stocks: [Stock]
    cov: [[float]]
    cor: [[float]]

    def __init__(self, stocks: [Stock], show: bool = False):
        self.stocks = stocks
        self.cov = self.cov(stocks, show)
        self.cor = self.cor(stocks, show)

    """
    This function calculates the variance x covariance matrix for a set of 
    stock selections.
    Ref: Covariance in Python -- https://datatofish.com/covariance-matrix-python/
    """

    @staticmethod
    def cov(stocks: [Stock], show: bool = False):
        cov = np.cov(np.array([stock.get_returns() for stock in stocks]))
        if show:
            sn.heatmap(cov, annot=True, fmt='.4g')
            plt.show()
        return cov

    @staticmethod
    def cor(stocks: [Stock], show: bool = False):
        cor = np.corrcoef(np.array([stock.get_returns() for stock in stocks]))
        if show:
            sn.heatmap(cor, annot=True, fmt='.4g')
            plt.show()
        return cor
