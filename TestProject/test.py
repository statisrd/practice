from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import pyqtgraph as pg
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2560, 1440))
        self.widget.setStyleSheet("background-color: rgb(5, 0, 26);")
        self.widget.setObjectName("widget")

        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 1080, 430))
        self.widget_2.setStyleSheet("background-color: rgb(21, 16, 43);\n"
                                    "border-radius: 20px;\n"
                                    "")
        self.widget_2.setObjectName("widget_2")

        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(720, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # trades
        self.trades = QtWidgets.QLabel(self.widget_2)
        self.trades.setGeometry(QtCore.QRect(920, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trades.setFont(font)
        self.trades.setStyleSheet("color: rgb(255, 255, 255);")
        self.trades.setObjectName("trades")

        self.trades_sell = QtWidgets.QLabel(self.widget_2)
        self.trades_sell.setGeometry(QtCore.QRect(870, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trades_sell.setFont(font)
        self.trades_sell.setStyleSheet("color: rgb(255, 255, 255);")
        self.trades_sell.setObjectName("trades_sell")

        self.trades_buy = QtWidgets.QLabel(self.widget_2)
        self.trades_buy.setGeometry(QtCore.QRect(970, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trades_buy.setFont(font)
        self.trades_buy.setStyleSheet("color: rgb(255, 255, 255);")
        self.trades_buy.setObjectName("trades_buy")

        self.trades_sell_price = QtWidgets.QLabel(self.widget_2)
        self.trades_sell_price.setGeometry(QtCore.QRect(870, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trades_sell_price.setFont(font)
        self.trades_sell_price.setStyleSheet("color: rgb(255, 255, 255);")
        self.trades_sell_price.setObjectName("trades_sell_price")

        self.trades_buy_price = QtWidgets.QLabel(self.widget_2)
        self.trades_buy_price.setGeometry(QtCore.QRect(970, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trades_buy_price.setFont(font)
        self.trades_buy_price.setStyleSheet("color: rgb(255, 255, 255);")
        self.trades_buy_price.setObjectName("trades_buy_price")

        #

        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(170, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(620, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        self.graphWidget = pg.PlotWidget(self.widget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 220, 781, 451))
        self.graphWidget.setObjectName("graphWidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Обновление информации о криптовалюте в реальном времени
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_crypto_info)
        self.timer.start(5000)  # Обновлять каждые 5 секунд

        self.update_crypto_info()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BTC"))
        self.label_2.setText(_translate("MainWindow", "24 h"))
        self.label_3.setText(_translate("MainWindow", "USD"))
        self.trades.setText(_translate("MainWindow", "trades"))
        self.trades_sell.setText(_translate("MainWindow", "sell"))
        self.trades_buy.setText(_translate("MainWindow", "buy"))

    def get_buy_value(self, coin1="btc", coin2="usd", limit=150):
        response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

        total_trade_bid = 0

        for item in response.json()[f"{coin1}_{coin2}"]:
            if item["type"] == "bid":
                total_trade_bid += item["price"] * item["amount"]

        return round(total_trade_bid, 2)

    def get_sell_value(self, coin1="btc", coin2="usd", limit=150):
        response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

        total_trade_ask = 0

        for item in response.json()[f"{coin1}_{coin2}"]:
            if item["type"] == "ask":
                total_trade_ask += item["price"] * item["amount"]

        return round(total_trade_ask, 2)

    def update_crypto_info(self):
        # Получение данных о текущей цене BTC
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        btc_data = response.json()
        if "bpi" in btc_data and "USD" in btc_data["bpi"]:
            btc_price = btc_data["bpi"]["USD"]["rate"]
            self.label_4.setText(btc_price)
        else:
            self.label_4.setText("0")

        # Получение данных о цене BTC за прошлую неделю
        response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart",
                                params={"vs_currency": "usd", "days": 7})
        btc_data = response.json()

        if "prices" in btc_data:
            prices = btc_data["prices"]
            timestamps = [price[0] for price in prices]
            prices = [price[1] for price in prices]

            # Вычисление изменения цены за последние 24 часа
            response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?for=yesterday")
            btc_data_yesterday = response.json()
            if "bpi" in btc_data_yesterday and btc_data_yesterday["bpi"]:
                yesterday_price = list(btc_data_yesterday["bpi"].values())[0]
                current_price = float(btc_price.replace(",", ""))
                price_change = current_price - yesterday_price
                price_change_percent = (price_change / yesterday_price) * 100
                self.label_5.setText(f"{price_change_percent:.2f}%")

                if price_change >= 0:
                    self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
                else:
                    self.label_5.setStyleSheet("color: rgb(0, 255, 0);")

            self.graphWidget.setBackground((21, 16, 43))
            self.plot_prices(timestamps, prices)
        else:
            self.label_5.setText("0")

        # Получение данных о трейдах
        self.trades_sell_price.setText(f"{self.get_sell_value():}")
        self.trades_buy_price.setText(f"{self.get_buy_value():}")

        self.trades_sell_price.setStyleSheet("color: rgb(0, 255, 0);")
        self.trades_buy_price.setStyleSheet("color: rgb(255, 0, 0);")

    def plot_prices(self, timestamps, prices):
        self.graphWidget.clear()
        self.graphWidget.plot(timestamps, prices, pen=(255, 255, 255))
        self.graphWidget.setLabel('left', 'Price (USD)')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setTitle('Bitcoin Price Change in the Last Week')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
