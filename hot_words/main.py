# coding:utf-8

import sys
import filter as f
import analyze
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.ui = analyze.Ui_analyze()
        self.ui.setupUi(self)
    
    def generate(self):
        try:
            sentences = []
            summary = {}
            #print(self.ui.input.toPlainText())
            self.ui.wordcloud.clear()
            self.ui.count.clear()
            input_url =  self.ui.input.toPlainText()
            input_url = input_url.split('\n')
            for i in input_url:
                sentences = sentences + f.get_labels(i)
            summary = f.count_label(sentences)
            for k, v in summary.items():
                self.ui.count.addItem(str(k) + ": " + str(v))
            tmp = f.connect_sentences(sentences)
            f.generate_word_cloud(tmp, width = 400, height = 400)
            pix = QPixmap(r'./word_cloud.png')
            self.ui.wordcloud.setPixmap(pix)
        except:
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    sys.exit(myapp.exec_())
