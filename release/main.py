import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from addEditCoffeeForm import Ui_Form
from main1 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.print_data()
        self.updat.clicked.connect(self.update_table)
        self.data = ''

    def print_data(self):
        self.con = sqlite3.connect('data/coffee.db')
        self.cur = self.con.cursor()
        self.drink = self.cur.execute('SELECT * from data').fetchall()
        self.data = ''
        for i in self.drink:
            self.data += f"ID {i[0]}, Название сорта {i[1]}, степень обжарки {i[2]}," \
                         f" {i[3]}, описание вкуса - {i[4]}, цена - {i[5]}, объем упаковки - {i[6]}\n"
        self.text.setPlainText(self.data)
        self.btn.clicked.connect(self.add_change)

    def add_change(self):
        self.ex1 = AddChangeWindow()
        self.updat.setStyleSheet("background-color: red")
        self.ex1.show()

    def update_table(self):
        self.updat.setStyleSheet("background-color: None")
        self.print_data()

class AddChangeWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.loadUi(self)
        self.add.clicked.connect(self.ADD)
        self.change.clicked.connect(self.CHANGE)

    def ADD(self):
        try:
            self.id = int(self.id_line.text())
            self.name = self.name_line.text()
            self.fry = self.fry_line.text()
            self.cond = self.cond_line.text()
            self.taste = self.taste_line.text()
            self.cost = int(self.cost_line.text())
            self.V = int(self.V_line.text())
            self.con = sqlite3.connect('coffee.db')
            self.cur = self.con.cursor()
            print(1)
            self.act = self.cur.execute(f'INSERT INTO data VALUES({self.id},"{self.name}","{self.fry}","{self.cond}"' +
                                        f',"{self.taste}",{self.cost}, {self.V})')
            self.con.commit()
        except:
            print('Неправильный формат данных')

    def CHANGE(self):
        try:
            self.id = int(self.id_line.text())
            print(1)
            self.name = self.name_line.text()
            print(2)
            self.fry = self.fry_line.text()
            print(self.fry)
            print(3)
            self.cond = self.cond_line.text()
            print(4)
            self.taste = self.taste_line.text()
            print(5)
            self.cost = self.cost_line.text()
            print(6)
            self.V = self.V_line.text()
            print(7)
            self.con = sqlite3.connect('coffee.db')
            self.cur = self.con.cursor()
            print(8)
            if len(self.name) > 0:
                self.cur.execute(
                    f'UPDATE data SET name_sort = "{self.name}" WHERE ID = {self.id}'
                )
                self.con.commit()
                print(9)
            if len(self.fry) > 0:
                self.cur.execute(
                    f'UPDATE data SET fry = "{self.fry}" WHERE ID = {self.id}'
                )
                print(10)
                self.con.commit()
            if len(self.cond) > 0:
                self.cur.execute(
                    f'UPDATE data SET condition = "{self.cond}" WHERE ID = {self.id}'
                )
                self.con.commit()
            if len(self.taste) > 0:
                self.cur.execute(
                    f'UPDATE data SET taste = "{self.taste}" WHERE ID = {self.id}'
                )
                self.con.commit()
            if len(self.cost) > 0:
                self.cur.execute(
                    f'UPDATE data SET cost = {int(self.cost)} WHERE ID = {self.id}'
                )
                self.con.commit()
            if len(self.V) > 0:
                self.cur.execute(
                    f'UPDATE data SET V = {int(self.V)} WHERE ID = {self.id}'
                )
                self.con.commit()
        except:
            print('Неправильный формат данных')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())