# app.py
from datetime import date

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
        print("Hello World...")


class Date:
    def __init__(self):
        pass


# Data represent a nominal percentage of change of a stock based on a specified date.
class Data:
    date: date
    percentage: float

    def __init__(self, date: date, percentage: float):
        self.date = date
        self.percentage = percentage


class Stock:
    ticker: str

    def __init__(self, ticker: str):
        self.ticker = ticker

    def __str__(self):
        return self.ticker


class Portfolio:
    stocks: [Stock]

    def __init__(self, stocks: [Stock]):
        self.stocks = stocks

    @staticmethod
    def run():
        print("Portfolio Manager")
