#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading 
import socket
import time
import sys
from PyQt5.QtWidgets import *

class TelloController1(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.initConnection()
        self.initUI()

    # 通信の設定
    def initConnection(self):
        host = ''
        port = 9000
        locaddr = (host,port) 
        self.tello = ('192.168.10.1', 8889)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(locaddr)

        # 受信スレッド起動
        recvThread = threading.Thread(target=self.recvSocket)
        recvThread.setDaemon(True)
        recvThread.start()

        # 最初にcommandコマンドを送信
        try:
            sent = self.sock.sendto('command'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    # UIの作成
    def initUI(self):
        self.label = QLabel('')
        self.label.setFrameStyle(QFrame.Box | QFrame.Plain)

        # 終了ボタン
        endBtn = QPushButton("End")
        endBtn.clicked.connect(self.endBtnClicked)

        # 離着陸ボタン
        takeoffBtn = QPushButton("Takeoff")
        takeoffBtn.clicked.connect(self.takeoffBtnClicked)
        landBtn = QPushButton("Land")
        landBtn.clicked.connect(self.landBtnClicked)

        # ボタンのレイアウト
        layout = QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(endBtn,0,1)
        layout.addWidget(takeoffBtn,1,0)
        layout.addWidget(landBtn,1,1)
        self.setLayout(layout)

    # 終了処理
    def endBtnClicked(self):
        sys.exit()

    # takeoffコマンド送信
    def takeoffBtnClicked(self):
        try:
            sent = self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    # landコマンド送信
    def landBtnClicked(self):
        try:
            sent = self.sock.sendto('land'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    # Telloからのレスポンス受信
    def recvSocket(self):
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                self.label.setText(data.decode(encoding="utf-8"))
            except:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelloController1()
    window.show()
    sys.exit(app.exec_())
