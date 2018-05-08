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
        # 速度を遅めに設定
        try:
            sent = self.sock.sendto('speed 50'.encode(encoding="utf-8"), self.tello)
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

        # 上昇下降回転ボタン
        upBtn = QPushButton("↑↑")
        upBtn.clicked.connect(self.upBtnClicked)
        downBtn = QPushButton("↓↓")
        downBtn.clicked.connect(self.downBtnClicked)
        cwBtn = QPushButton("→↓")
        cwBtn.clicked.connect(self.cwBtnClicked)
        ccwBtn = QPushButton("↓←")
        ccwBtn.clicked.connect(self.ccwBtnClicked)

        # 前後左右ボタン
        forwardBtn = QPushButton("↑")
        forwardBtn.clicked.connect(self.forwardBtnClicked)
        backBtn = QPushButton("↓")
        backBtn.clicked.connect(self.backBtnClicked)
        rightBtn = QPushButton("→")
        rightBtn.clicked.connect(self.rightBtnClicked)
        leftBtn = QPushButton("←")
        leftBtn.clicked.connect(self.leftBtnClicked)

        batteryBtn = QPushButton("Battery?")
        batteryBtn.clicked.connect(self.batteryBtnClicked)
        timeBtn = QPushButton("Time?")
        timeBtn.clicked.connect(self.timeBtnClicked)

        # ボタンのレイアウト
        layout = QGridLayout()
        layout.addWidget(self.label,0,0)
        layout.addWidget(endBtn,0,6)
        layout.addWidget(takeoffBtn,0,3)
        layout.addWidget(landBtn,1,3)

        layout.addWidget(upBtn,2,1)
        layout.addWidget(downBtn,4,1)
        layout.addWidget(cwBtn,3,2)
        layout.addWidget(ccwBtn,3,0)

        layout.addWidget(forwardBtn,2,5)
        layout.addWidget(backBtn,4,5)
        layout.addWidget(rightBtn,3,6)
        layout.addWidget(leftBtn,3,4)

        layout.addWidget(batteryBtn,0,2)
        layout.addWidget(timeBtn,0,4)

        self.setLayout(layout)

    # 終了処理
    def endBtnClicked(self):
        sys.exit()

    # 各種コマンド送信
    def takeoffBtnClicked(self):
        try:
            sent = self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def landBtnClicked(self):
        try:
            sent = self.sock.sendto('land'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def upBtnClicked(self):
        try:
            sent = self.sock.sendto('up 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def downBtnClicked(self):
        try:
            sent = self.sock.sendto('down 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def cwBtnClicked(self):
        try:
            sent = self.sock.sendto('cw 45'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def ccwBtnClicked(self):
        try:
            sent = self.sock.sendto('ccw 45'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def forwardBtnClicked(self):
        try:
            sent = self.sock.sendto('forward 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def backBtnClicked(self):
        try:
            sent = self.sock.sendto('back 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def rightBtnClicked(self):
        try:
            sent = self.sock.sendto('right 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def leftBtnClicked(self):
        try:
            sent = self.sock.sendto('left 20'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def batteryBtnClicked(self):
        try:
            sent = self.sock.sendto('battery?'.encode(encoding="utf-8"), self.tello)
        except:
            pass
    def timeBtnClicked(self):
        try:
            sent = self.sock.sendto('time?'.encode(encoding="utf-8"), self.tello)
        except:
            pass

    # Telloからのレスポンス受信
    def recvSocket(self):
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                self.label.setText(data.decode(encoding="utf-8").strip())
            except:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelloController1()
    window.show()
    sys.exit(app.exec_())
