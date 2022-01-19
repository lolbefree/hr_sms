#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys
from datetime import date, datetime
from pprint import pprint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from collections import Counter
from untitled import Ui_InterviewInvitation
import not_for_git
import os
import os
import sys
import requests


class Convertor(QtWidgets.QMainWindow):
    def __init__(self, filename):
        self.ui = Ui_InterviewInvitation()
        super().__init__()
        self.ui.setupUi(self)
        self.now = datetime.now()
        self.today = date.today()
        self.file_name = filename
        user_profile = os.environ['USERPROFILE']
        user_desktop = user_profile + "\\Desktop"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if not os.path.isfile(f'{user_desktop}\\{self.file_name}'):
            self.file = open(f'{user_desktop}\\{self.file_name}', 'w+')
        else:
            print(user_desktop)
            self.file = open(f'{user_desktop}\\{self.file_name}', 'r')
            str_to_textedit = "".join(self.file.readlines())
            self.ui.textEdit.setPlainText(str_to_textedit)
        self.ui.pushButton.clicked.connect(lambda x: self.send_sms(self.ui.to_phone.text(), self.ui.textEdit.toPlainText()))


    def send_sms(self, to, text):
        # text = text.replace("\n", " ")
        print(to, text)
        ret = QMessageBox.question(self, 'Надіслати повідомлення??!',
                                   f"'Надіслати повідомлення на номер {to}?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            requests.get(f"https://api.turbosms.ua/message/send.json?recipients[0]=38{to}&sms[sender]=AVTOSOJUZ&sms[text]={text}&token={not_for_git.token}")
            self.ui.res.setText("Повідомлення надіслано!")
            self.ui.res.setStyleSheet("color: green")


def main():
    app = QApplication(sys.argv)
    w = Convertor("sms_example.conf")
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()
