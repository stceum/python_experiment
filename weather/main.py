# coding:utf-8

import sys
import weather_com_cn as w
import weather
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    city_dict = []
    city_code = -1

    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.ui = weather.Ui_weather()
        self.ui.setupUi(self)
    
    def get_weather_list(self):
        try:
            self.ui.warning.setText("please wait...")
            city = w.search(self.ui.search.toPlainText())
            self.ui.select.clear()
            self.city_dict = []
            for k,v in city.items():
                self.city_dict.append(v)
                self.ui.select.addItem(k)
            self.ui.warning.setText("done!")
        except:
            self.ui.warning.setText("an error happens while fetching list!")
    
    def get_weather(self):
        self.ui.warning.setText("please wait...")
        try:
            #print(self.ui.select.currentRow())
            self.city_code = self.city_dict[self.ui.select.currentRow()]
            #print(self.city_code)
            info = w.get_weather(self.city_code)
            #print(info)
            self.ui.time0.setText(info[0]['time'])
            self.ui.wea0.setText(info[0]['wea'])
            pix = QPixmap(r'./pic/' + info[0]['weap'] + r'.png')
            self.ui.weap0.setPixmap(pix)
            self.ui.tem0.setText(info[0]['tem'])
            self.ui.win0.setText(info[0]['win'])
            pix = QPixmap(r'./pic/' + info[0]['winp'] + r'.png')
            self.ui.winp0.setPixmap(pix)
            self.ui.suntime0.setText(info[0]['suntime'])
            # night
            self.ui.time1.setText(info[1]['time'])
            self.ui.wea1.setText(info[1]['wea'])
            pix = QPixmap(r'./pic/' + info[1]['weap'] + r'.png')
            self.ui.weap1.setPixmap(pix)
            self.ui.tem1.setText(info[1]['tem'])
            self.ui.win1.setText(info[1]['win'])
            pix = QPixmap(r'./pic/' + info[1]['winp'] + r'.png')
            self.ui.winp1.setPixmap(pix)
            self.ui.suntime1.setText(info[1]['suntime'])
            self.ui.warning.setText("done!")
        except:
            self.ui.time0.clear()
            self.ui.wea0.clear()
            self.ui.weap0.clear()
            self.ui.tem0.clear()
            self.ui.win0.clear()
            self.ui.winp0.clear()
            self.ui.suntime0.clear()
            self.ui.time1.clear()
            self.ui.wea1.clear()
            self.ui.weap1.clear()
            self.ui.tem1.clear()
            self.ui.win1.clear()
            self.ui.winp1.clear()
            self.ui.suntime1.clear()
            
            self.ui.warning.setText("404 not found")

    
if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    sys.exit(myapp.exec_())
