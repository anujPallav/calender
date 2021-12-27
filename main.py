from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout(self)
        self.date_time = datetime.now()
        self.date_container = []

        self.pixmap = QPixmap('./calander_background.jpg')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.pixmap)
        self.background_label.resize(400,300)
    
        self.date_ = self.date_time.strftime('%d')
        self.day_ = self.date_time.strftime('%A')
        self.mounth_ = self.date_time.strftime('%b')

        self.value = 31
        self.count = 0
        self.row = 0
        self.col = 0

        while self.value >= 1:
            self.value -=1
            self.count += 1
            self.col += 1
            if self.col >= 8:
                self.row += 1
                self.col = 0
            
            self.new_date_label = QLabel(f'{self.count}')
            self.grid_layout.addWidget(self.new_date_label, self.row, self.col)
            self.date_container.append(self.new_date_label.text())
            if self.new_date_label.text() == self.date_:
                self.today_date_style()

        self.day_m = f'{self.day_}:{self.mounth_}'
        self.day_m_label = QLabel(self)
        self.day_m_label.setText(self.day_m)
        self.day_m_label.move(280,0)
        
        self.setWindowIcon(QIcon('./calander.png'))
        self.setLayout(self.grid_layout)
        self.setFixedSize(400, 300)
        self.show()

        self.desigen_function()
        self.d_m_desigen()

    def today_date_style(self):
        self.new_date_label.setStyleSheet(f'font:bold 15px; font-family:Comic Sans MS, Comic Sans, cursive; color:#6C3483;')

    def desigen_function(self):
        self.setStyleSheet(f'font:13px; font-family:Ink Free;')
    
    def d_m_desigen(self):
        self.day_m_label.setStyleSheet(f'font:bold 18px;')
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
