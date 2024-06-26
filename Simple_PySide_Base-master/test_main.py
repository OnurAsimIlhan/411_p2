from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QPoint, Qt
import requests

from PyQt5.QtWidgets import *
from db_connection import *
from datetime import datetime

FULL_PATH = "Simple_PySide_Base-master/storage/bookmarking.db"

class Ui_MainWindow(object):
        

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1000, 720)
                MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
                brush.setStyle(QtCore.Qt.NoBrush)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
                brush.setStyle(QtCore.Qt.NoBrush)
                palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
                brush = QtGui.QBrush(QtGui.QColor(66, 73, 90))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
                brush = QtGui.QBrush(QtGui.QColor(55, 61, 75))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
                brush = QtGui.QBrush(QtGui.QColor(29, 32, 40))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
                brush = QtGui.QBrush(QtGui.QColor(22, 24, 30))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
                brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
                brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
                brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(44, 49, 60))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
                brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
                brush.setStyle(QtCore.Qt.NoBrush)
                palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
                MainWindow.setPalette(palette)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(10)
                MainWindow.setFont(font)
                MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
        "QToolTip {\n"
        "    color: #ffffff;\n"
        "    background-color: rgba(27, 29, 35, 160);\n"
        "    border: 1px solid rgb(40, 40, 40);\n"
        "    border-radius: 2px;\n"
        "}")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("background: transparent;\n"
        "color: rgb(210, 210, 210);")
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
                self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.frame_main = QtWidgets.QFrame(self.centralwidget)
                self.frame_main.setStyleSheet("/* LINE EDIT */\n"
        "QLineEdit {\n"
        "    background-color: rgb(27, 29, 35);\n"
        "    border-radius: 5px;\n"
        "    border: 2px solid rgb(27, 29, 35);\n"
        "    padding-left: 10px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    border: 2px solid rgb(91, 101, 124);\n"
        "}\n"
        "\n"
        "/* SCROLL BARS */\n"
        "QScrollBar:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    height: 14px;\n"
        "    margin: 0px 21px 0 21px;\n"
        "    border-radius: 0px;\n"
        "}\n"
        "QScrollBar::handle:horizontal {\n"
        "    background: rgb(85, 170, 255);\n"
        "    min-width: 25px;\n"
        "    border-radius: 7px\n"
        "}\n"
        "QScrollBar::add-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        "    border-top-right-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "    subcontrol-position: right;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::sub-line:horizontal {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "    width: 20px;\n"
        "    border-top-left-radius: 7px;\n"
        "    border-bottom-left-radius: 7px;\n"
        "    subcontrol-position: left;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
        "{\n"
        "     background: none;\n"
        "}\n"
        " QScrollBar:vertical {\n"
        "    border: none;\n"
        "    background: rgb(52, 59, 72);\n"
        "    width: 14px;\n"
        "    margin: 21px 0 21px 0;\n"
        "    border-radius: 0px;\n"
        " }\n"
        " QScrollBar::handle:vertical {    \n"
        "    background: rgb(85, 170, 255);\n"
        "    min-height: 25px;\n"
        "    border-radius: 7px\n"
        " }\n"
        " QScrollBar::add-line:vertical {\n"
        "     border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "     height: 20px;\n"
        "    border-bottom-left-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "     subcontrol-position: bottom;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::sub-line:vertical {\n"
        "    border: none;\n"
        "    background: rgb(55, 63, 77);\n"
        "     height: 20px;\n"
        "    border-top-left-radius: 7px;\n"
        "    border-top-right-radius: 7px;\n"
        "     subcontrol-position: top;\n"
        "     subcontrol-origin: margin;\n"
        " }\n"
        " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
        "     background: none;\n"
        " }\n"
        "\n"
        "/* CHECKBOX */\n"
        "QCheckBox::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "    width: 15px;\n"
        "    height: 15px;\n"
        "    border-radius: 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QCheckBox::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QCheckBox::indicator:checked {\n"
        "    background: 3px solid rgb(52, 59, 72);\n"
        "    border: 3px solid rgb(52, 59, 72);    \n"
        "    background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
        "}\n"
        "\n"
        "/* RADIO BUTTON */\n"
        "QRadioButton::indicator {\n"
        "    border: 3px solid rgb(52, 59, 72);\n"
        "    width: 15px;\n"
        "    height: 15px;\n"
        "    border-radius: 10px;\n"
        "    background: rgb(44, 49, 60);\n"
        "}\n"
        "QRadioButton::indicator:hover {\n"
        "    border: 3px solid rgb(58, 66, 81);\n"
        "}\n"
        "QRadioButton::indicator:checked {\n"
        "    background: 3px solid rgb(94, 106, 130);\n"
        "    border: 3px solid rgb(52, 59, 72);    \n"
        "}\n"
        "\n"
        "/* COMBOBOX */\n"
        "QComboBox{\n"
        "    background-color: rgb(27, 29, 35);\n"
        "    border-radius: 5px;\n"
        "    border: 2px solid rgb(27, 29, 35);\n"
        "    padding: 5px;\n"
        "    padding-left: 10px;\n"
        "}\n"
        "QComboBox:hover{\n"
        "    border: 2px solid rgb(64, 71, 88);\n"
        "}\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 25px; \n"
        "    border-left-width: 3px;\n"
        "    border-left-color: rgba(39, 44, 54, 150);\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;    \n"
        "    background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
        "    background-position: center;\n"
        "    background-repeat: no-reperat;\n"
        " }\n"
        "QComboBox QAbstractItemView {\n"
        "    color: rgb(85, 170, 255);    \n"
        "    background-color: rgb(27, 29, 35);\n"
        "    padding: 10px;\n"
        "    selection-background-color: rgb(39, 44, 54);\n"
        "}\n"
        "\n"
        "/* SLIDERS */\n"
        "QSlider::groove:horizontal {\n"
        "    border-radius: 9px;\n"
        "    height: 18px;\n"
        "    margin: 0px;\n"
        "    background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:horizontal:hover {\n"
        "    background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:horizontal {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "    border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        "QSlider::groove:vertical {\n"
        "    border-radius: 9px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "    background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QSlider::groove:vertical:hover {\n"
        "    background-color: rgb(55, 62, 76);\n"
        "}\n"
        "QSlider::handle:vertical {\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    border: none;\n"
        "    height: 18px;\n"
        "    width: 18px;\n"
        "    margin: 0px;\n"
        "    border-radius: 9px;\n"
        "}\n"
        "QSlider::handle:vertical:hover {\n"
        "    background-color: rgb(105, 180, 255);\n"
        "}\n"
        "QSlider::handle:vertical:pressed {\n"
        "    background-color: rgb(65, 130, 195);\n"
        "}\n"
        "\n"
        "")
                self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_main.setObjectName("frame_main")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.frame_top = QtWidgets.QFrame(self.frame_main)
                self.frame_top.setMinimumSize(QtCore.QSize(0, 65))
                self.frame_top.setMaximumSize(QtCore.QSize(16777215, 65))
                self.frame_top.setStyleSheet("background-color: transparent;")
                self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_top.setObjectName("frame_top")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.frame_toggle = QtWidgets.QFrame(self.frame_top)
                self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
                self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
                self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_toggle.setObjectName("frame_toggle")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_toggle)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
                self.btn_toggle_menu.setSizePolicy(sizePolicy)
                self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
        "    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
        "    background-position: center;\n"
        "    background-repeat: no-reperat;\n"
        "    border: none;\n"
        "    background-color: rgb(27, 29, 35);\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(33, 37, 43);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    background-color: rgb(85, 170, 255);\n"
        "}")
                self.btn_toggle_menu.setText("")
                self.btn_toggle_menu.setObjectName("btn_toggle_menu")
                self.verticalLayout_3.addWidget(self.btn_toggle_menu)
                self.horizontalLayout_3.addWidget(self.frame_toggle)
                self.frame_top_right = QtWidgets.QFrame(self.frame_top)
                self.frame_top_right.setStyleSheet("background: transparent;")
                self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_top_right.setObjectName("frame_top_right")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top_right)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
                self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 42))
                self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
                self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_top_btns.setObjectName("frame_top_btns")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_btns)
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_4.setSpacing(0)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
                self.frame_label_top_btns.setSizePolicy(sizePolicy)
                self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_label_top_btns.setObjectName("frame_label_top_btns")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
                self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
                self.horizontalLayout_10.setSpacing(0)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
                self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
                self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
        "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
        "background-position: center;\n"
        "background-repeat: no-repeat;\n"
        "")
                self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
                self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
                self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label_title_bar_top.setFont(font)
                self.label_title_bar_top.setStyleSheet("background: transparent;\n"
        "")
                self.label_title_bar_top.setObjectName("label_title_bar_top")
                self.horizontalLayout_10.addWidget(self.label_title_bar_top)
                self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
                self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
                self.frame_btns_right.setSizePolicy(sizePolicy)
                self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
                self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_btns_right.setObjectName("frame_btns_right")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setSpacing(0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
                self.btn_minimize.setSizePolicy(sizePolicy)
                self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
                self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
                self.btn_minimize.setStyleSheet("QPushButton {    \n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    background-color: rgb(85, 170, 255);\n"
        "}")
                self.btn_minimize.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btn_minimize.setIcon(icon)
                self.btn_minimize.setObjectName("btn_minimize")
                self.horizontalLayout_5.addWidget(self.btn_minimize)
                self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
                self.btn_maximize_restore.setSizePolicy(sizePolicy)
                self.btn_maximize_restore.setMinimumSize(QtCore.QSize(40, 0))
                self.btn_maximize_restore.setMaximumSize(QtCore.QSize(40, 16777215))
                self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    background-color: rgb(85, 170, 255);\n"
        "}")
                self.btn_maximize_restore.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btn_maximize_restore.setIcon(icon1)
                self.btn_maximize_restore.setObjectName("btn_maximize_restore")
                self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
                self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
                self.btn_close.setSizePolicy(sizePolicy)
                self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
                self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
                self.btn_close.setStyleSheet("QPushButton {    \n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(52, 59, 72);\n"
        "}\n"
        "QPushButton:pressed {    \n"
        "    background-color: rgb(85, 170, 255);\n"
        "}")
                self.btn_close.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btn_close.setIcon(icon2)
                self.btn_close.setObjectName("btn_close")
                self.horizontalLayout_5.addWidget(self.btn_close)
                self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_2.addWidget(self.frame_top_btns)
                self.frame_top_info = QtWidgets.QFrame(self.frame_top_right)
                self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
                self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
                self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_top_info.setObjectName("frame_top_info")

                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
                self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
                self.horizontalLayout_8.setSpacing(0)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")

                self.bookmark = QtWidgets.QPushButton()
                self.bookmark.setIcon(QIcon(r"Simple_PySide_Base-master\icons\bookmark.png"))
                self.bookmark.setMinimumHeight(35)

                self.go_btn = QtWidgets.QPushButton("Go")
                self.go_btn.setMinimumHeight(35)

                self.back_btn = QtWidgets.QPushButton("<")
                self.back_btn.setMinimumHeight(35)

                self.forward_btn = QtWidgets.QPushButton(">")
                self.forward_btn.setMinimumHeight(35)

                        

                self.label_top_info_1 = QtWidgets.QTextEdit(self.frame_top_info)
                self.label_top_info_1.setMaximumSize(QtCore.QSize(16777215, 35))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_top_info_1.setAlignment(QtCore.Qt.AlignCenter)

                font.setFamily("Segoe UI")
                self.label_top_info_1.setFont(font)
                self.label_top_info_1.setStyleSheet("color: rgb(255, 255, 255); ")
                self.label_top_info_1.setObjectName("label_top_info_1")
                self.horizontalLayout_8.addWidget(self.label_top_info_1)
                        
                self.horizontalLayout_8.addWidget(self.bookmark)
                self.horizontalLayout_8.addWidget(self.go_btn)
                self.horizontalLayout_8.addWidget(self.back_btn)
                self.horizontalLayout_8.addWidget(self.forward_btn)

                
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setBold(True)
                font.setWeight(75)
        
                self.verticalLayout_2.addWidget(self.frame_top_info)
                self.horizontalLayout_3.addWidget(self.frame_top_right)
                self.verticalLayout.addWidget(self.frame_top)
                self.frame_center = QtWidgets.QFrame(self.frame_main)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
                self.frame_center.setSizePolicy(sizePolicy)
                self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
                self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_center.setObjectName("frame_center")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
                self.frame_left_menu.setSizePolicy(sizePolicy)
                self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
                self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
                self.frame_left_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
                self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_left_menu.setObjectName("frame_left_menu")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_left_menu)
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_5.setSpacing(1)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.frame_menus = QtWidgets.QFrame(self.frame_left_menu)
                self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_menus.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_menus.setObjectName("frame_menus")
                self.layout_menus = QtWidgets.QVBoxLayout(self.frame_menus)
                self.layout_menus.setContentsMargins(0, 0, 0, 0)
                self.layout_menus.setSpacing(0)
                self.layout_menus.setObjectName("layout_menus")
                self.verticalLayout_5.addWidget(self.frame_menus, 0, QtCore.Qt.AlignTop)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                
                
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(12)
               
                self.horizontalLayout_2.addWidget(self.frame_left_menu)
                self.frame_content_right = QtWidgets.QFrame(self.frame_center)
                self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
                self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_content_right.setObjectName("frame_content_right")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.frame_content = QtWidgets.QFrame(self.frame_content_right)
                self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_content.setObjectName("frame_content")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content)
                self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
                self.verticalLayout_9.setSpacing(0)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout()
                self.verticalLayout_7.setObjectName("verticalLayout_7")

                self.browser = QWebEngineView()
                self.verticalLayout_7.addWidget(self.browser)
                self.browser.setUrl(QUrl("http://google.com"))
                self.browser.urlChanged.connect(self.update_window_title)
                self.go_btn.clicked.connect(lambda: self.navigate(self.label_top_info_1.toPlainText()))
                self.back_btn.clicked.connect(self.browser.back)
                self.forward_btn.clicked.connect(self.browser.forward)
                self.bookmark.clicked.connect(self.bookmark_add_new)

                self.verticalLayout_9.addLayout(self.verticalLayout_7)
                self.verticalLayout_4.addWidget(self.frame_content)
                self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
                self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
                self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
                self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
                self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_grip.setObjectName("frame_grip")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
                self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
                self.horizontalLayout_6.setSpacing(0)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
                self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_label_bottom.setObjectName("frame_label_bottom")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
                self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
                self.horizontalLayout_7.setSpacing(0)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                self.label_credits.setFont(font)
                self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
                self.label_credits.setObjectName("label_credits")
                self.horizontalLayout_7.addWidget(self.label_credits)
                self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
                self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                self.label_version.setFont(font)
                self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
                self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.label_version.setObjectName("label_version")
                self.horizontalLayout_7.addWidget(self.label_version)
                self.horizontalLayout_6.addWidget(self.frame_label_bottom)
                self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
                self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
                self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
        "    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
        "    background-position: center;\n"
        "    background-repeat: no-reperat;\n"
        "}")
                self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_size_grip.setObjectName("frame_size_grip")
                self.horizontalLayout_6.addWidget(self.frame_size_grip)
                self.verticalLayout_4.addWidget(self.frame_grip)
                self.horizontalLayout_2.addWidget(self.frame_content_right)
                self.verticalLayout.addWidget(self.frame_center)
                self.horizontalLayout.addWidget(self.frame_main)


                MainWindow.setCentralWidget(self.centralwidget)



                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
                MainWindow.setTabOrder(self.btn_maximize_restore, self.btn_close)
                MainWindow.setTabOrder(self.btn_close, self.btn_toggle_menu)

                
                

                # Get bookmarks from database
                connection, cursor = create_connection(FULL_PATH)
                select_query = "SELECT * FROM Bookmarks"
                cursor.execute(select_query)
                connection.commit()
                records = cursor.fetchall()
                
                dt = datetime.now()
                current_day_of_week = dt.weekday()
                print(current_day_of_week)


                records = sorted(records, key=lambda x: x[current_day_of_week+2], reverse=False)
                def download_icon(url):
                        try:
                                response = requests.get(url)
                                if response.status_code == 200:
                                        pixmap = QPixmap()
                                        pixmap.loadFromData(response.content)
                                        return pixmap
                        except Exception as e:
                                print(f"Error downloading icon: {e}")
                        return QIcon(r"Simple_PySide_Base-master\icons\bookmark.png")
                def populate_bookmark(records):
                        for row in records:
                                truncated_name = row[0]

                                # Main button
                                button = QtWidgets.QPushButton(truncated_name)
                                
                                button.setProperty("bookmarkTitle", truncated_name)
                                
                                button.clicked.connect(lambda _, b=button: self.handle_bookmark(b))
                                icon_pixmap = download_icon(row[9])
                                if icon_pixmap:
                                        button.setIcon(QIcon(icon_pixmap))
                                        print("success")
                                button.setMinimumHeight(45)
                                button.setMinimumWidth(45)
                                button.setStyleSheet("font-size:16px; background-color: #323336;")

                                # X button
                                x_button = QtWidgets.QPushButton('X')
                                x_button.setVisible(False)

                                x_button.clicked.connect(lambda _, b=button: self.remove_bookmark(b))
                                x_button.setStyleSheet("font-size:16px; color: red;background-color: #323336")
                                x_button.setMinimumHeight(45)
                                x_button.setMinimumWidth(45)

                                x_button.setMaximumHeight(45)
                                x_button.setMaximumWidth(45)

                                # Create a horizontal layout
                                horizontal_layout15 = QtWidgets.QHBoxLayout()
                                # Add both buttons to the horizontal layout
                                horizontal_layout15.addWidget(button)
                                horizontal_layout15.addWidget(x_button)
                                button.setProperty("originalText", truncated_name)
                                # Add the horizontal layout to the vertical layout

                                width = self.frame_left_menu.width()
                                if(width == 70):
                                        x_button.setVisible(False)
                                        button.setText('')
                                
                                else:
                                        button.setText(button.property("originalText"))

                                self.verticalLayout_5.insertLayout(0,horizontal_layout15)

                populate_bookmark(records)
                
                label = QtWidgets.QPushButton("  My Bookmarks")
                label.setStyleSheet("font-size: 20px; text-align: left; font-weight: bold;")
                width = self.frame_left_menu.width()
                if(width == 70):
                       label.setVisible(False)  # Make the button not clickable
                
                label.setMinimumHeight(45)
                horizontal_layout15 = QtWidgets.QHBoxLayout()
                horizontal_layout15.addWidget(label)
                horizontal_layout15.setContentsMargins(0, 2, 0, 10)
                self.verticalLayout_5.insertLayout(0,horizontal_layout15)


                label = QtWidgets.QPushButton("CBA Browser")

                
                label.setIcon(QIcon(r"Simple_PySide_Base-master\icons\bookmark.png"))
                label.setIconSize(label.sizeHint())
                label.setProperty("originalText", "CBA Browser")
                label.setStyleSheet("font-size: 15px;  font-weight: bold;")
                width = self.frame_left_menu.width()
                if(width == 70):
                       label.setText('')
                       
                else:
                       label.setText(label.property("originalText"))
                label.setMinimumHeight(80)
                horizontal_layout15 = QtWidgets.QHBoxLayout()
                horizontal_layout15.addWidget(label)
                horizontal_layout15.setContentsMargins(0, 2, 0, 10)
                self.verticalLayout_5.insertLayout(-1,horizontal_layout15)
                connection.close()
                
                
        def handle_enter_key(self):
                # Get the text from label_top_info_1
                url = self.label_top_info_1.toPlainText()

                # Your logic for navigating to the URL
                self.navigate(url)

        def navigate(self, url):
                if url.startswith("~g"):
                        words = url.split()
                        # Check if there is at least one more word after "~g"
                        if len(words) > 1:
                        # Extract the second word (index 1)
                                command = words[1]
                                url = "http://www.google.com/search?q=" + command
                                self.label_top_info_1.setText(url)
                                self.browser.setUrl(QUrl(url))
                        else:
                                print("Command missing after ~g")
                        return
                if url.startswith("~y"):
                        words = url.split()
                        # Check if there is at least one more word after "~g"
                        if len(words) > 1:
                        # Extract the second word (index 1)
                                command = words[1]
                                url = "http://www.youtube.com/results?search_query=" + command
                                self.label_top_info_1.setText(url)
                                self.browser.setUrl(QUrl(url))
                        else:
                                print("Command missing after ~y")
                        return
                       
                if not url.startswith("http"):
                        url = "http://" + url
                self.label_top_info_1.setText(url)
                self.browser.setUrl(QUrl(url))
                
        def update_window_title(self, url):
                current_url = self.browser.url().toString()

                if not current_url.startswith("http"):
                        current_url = "http://" + current_url
                self.label_top_info_1.setText(current_url)
                self.label_top_info_1.setText(current_url)
        
        global FIRST_TIME
        FIRST_TIME = True
        global COUNTER
        COUNTER = 0

        START_TIME = True
        def bookmark_add_new(self):
                global FIRST_TIME
                global COUNTER
                if(FIRST_TIME):
                        label = QtWidgets.QPushButton("  Recently Added")
                        width = self.frame_left_menu.width()
                        if(width == 70):
                                label.setVisible(False)  # Make the button not clickable
                        label.setStyleSheet("font-size: 20px; text-align: left; font-weight: bold;")
                        label.setDisabled(True)  # Make the button not clickable
                        label.setMinimumHeight(60)
                        horizontal_layout15 = QtWidgets.QHBoxLayout()
                        horizontal_layout15.addWidget(label)
                        horizontal_layout15.setContentsMargins(0, 2, 0, 10)
                        FIRST_TIME=False
                        self.verticalLayout_5.insertLayout(0,horizontal_layout15)

                
                def download_icon(url):
                        
                        try:
                                response = requests.get(url)
                                if response.status_code == 200:
                                        pixmap = QPixmap()
                                        pixmap.loadFromData(response.content)
                                        return pixmap
                        except Exception as e:
                                print(f"Error downloading icon: {e}")
                        return QIcon(r"Simple_PySide_Base-master\icons\bookmark.png")

                
                current_url = self.browser.url().toString()
                current_name = self.browser.title()
                icon_url = self.browser.iconUrl().url()
                print(icon_url)
                dt = datetime.now()
                current_day = dt.strftime('%A')

                connection, cursor = create_connection(FULL_PATH)
                check_query = f"SELECT COUNT(*) FROM Bookmarks WHERE url = '{current_url}';"
                cursor.execute(check_query)
                result = cursor.fetchone()
                if result and result[0] > 0:
                        print("Bookmark already exists.")
                        return

                insert_query = f"INSERT INTO Bookmarks (name, url, {current_day}, icon_url) VALUES ('{current_name}', '{current_url}', 1, '{icon_url}');"
                COUNTER = COUNTER + 1
                cursor.execute(insert_query)
                connection.commit()
                connection.close()

                truncated_name = current_name
                button = QtWidgets.QPushButton(truncated_name)
                button.setProperty("bookmarkTitle", truncated_name)
                button.setStyleSheet("font-size:13px;")
                button.clicked.connect(lambda: self.handle_bookmark(button))

                icon_pixmap = download_icon(icon_url)
                if icon_pixmap:
                        button.setIcon(QIcon(icon_pixmap))     
                        print("success")
                
                # Set a horizontal layout for the button with icon to the left of text
                button.setMinimumHeight(45)
                button.setStyleSheet("font-size:16px; background-color:#323336")
                # X button
                x_button = QtWidgets.QPushButton('X')
                
                x_button.clicked.connect(lambda _, b=button: self.remove_bookmark(b))
                x_button.setStyleSheet("font-size:16px; color: red;background-color: #323336;")
                x_button.setMinimumHeight(45)
                x_button.setMinimumWidth(45)

                x_button.setMaximumHeight(45)
                x_button.setMaximumWidth(45)
                horizontal_layout15 = QtWidgets.QHBoxLayout()

                # Add both buttons to the horizontal layout
                horizontal_layout15.addWidget(button)
                horizontal_layout15.addWidget(x_button)
                button.setProperty("originalText", truncated_name)

                width = self.frame_left_menu.width()
                if(width == 70):
                       x_button.setVisible(False)
                       button.setText('')
                       
                else:
                       button.setText(button.property("originalText"))
                # Add the horizontal layout to the vertical layout
                self.verticalLayout_5.insertLayout(1,horizontal_layout15)
                # Add the horizontal layout to the vertical layout
                self.newIcon = QtWidgets.QLabel(self.frame_left_menu)
                       
        
        def handle_bookmark(self, button: QtWidgets.QPushButton):
                main_button = button.property("bookmarkTitle")
                print(main_button)
                if main_button:
                        bookmark_name = main_button
                        print(bookmark_name)
                        connection, cursor = create_connection(FULL_PATH)

                        current_day = datetime.now().strftime('%A')
                        update_query = f"UPDATE Bookmarks SET {current_day} = {current_day} + 1 WHERE name = '{bookmark_name}';"
                        cursor.execute(update_query)
                        connection.commit()

                        select_query = f"SELECT * FROM Bookmarks WHERE name='{bookmark_name}'"
                        cursor.execute(select_query)
                        connection.commit()
                        records = cursor.fetchall()
                        connection.close()

                        print(records)

                        url = records[0][1]
                        print(url)
                        self.navigate(url)
                else:
                        print("Error: mainButton property not found")

           

        def remove_bookmark(self, button: QtWidgets.QPushButton):
                global COUNTER
                global FIRST_TIME
                bookmark_name = button.text()
                connection, cursor = create_connection(FULL_PATH)
                try:
                        delete_query = f"DELETE FROM Bookmarks WHERE name='{bookmark_name}'"
                        result = cursor.execute(delete_query)
                        connection.commit()
                        print(result)
                        print(f"Bookmark '{bookmark_name}' removed successfully.")
                        COUNTER = COUNTER - 1
                        for i in range(self.verticalLayout_5.count()):
                                item = self.verticalLayout_5.itemAt(i)
                                if isinstance(item, QtWidgets.QHBoxLayout):
                                        layout = item
                                        for j in range(layout.count()):
                                                if layout.itemAt(j).widget() == button:
                                                        layout.itemAt(j).widget().deleteLater()
                                                        layout.itemAt(j+1).widget().deleteLater()
                                                        layout.removeItem(layout.itemAt(j))
                                                        layout.removeItem(layout.itemAt(j))
                                                        layout.deleteLater()
                                                        self.verticalLayout_5.update()
                                                        # Remove "Recently added" label if no new additions
                                                        
                                                        return
                except Exception as e:
                        print(f"Error removing bookmark '{bookmark_name}': {e}")
                finally:
                        connection.close()
        
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_title_bar_top.setText(_translate("MainWindow", "Main Window"))
                self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
                self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
                self.btn_close.setToolTip(_translate("MainWindow", "Close"))
                
                self.label_top_info_1.setText(_translate("MainWindow", "http://google.com"))
                
                self.label_version.setText(_translate("MainWindow", "v1.0.0"))
    

     

import files_rc


def toggleMenu(self, maxWidth, enable):
        global FIRST_TIME
        if enable:
            # GET WIDTH
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            

            all_buttons = self.frame_left_menu.findChildren(QPushButton)
            for button in all_buttons:
                if button.text() == 'X':
                       button.setVisible(width == 70)
                elif button.text() == '  Recently Added':
                        button.setVisible(width == 70 and FIRST_TIME == False )

                elif button.text() == '  My Bookmarks':
                        button.setVisible(width == 70)
                
                else:
                        if width == 70:
                                button.setText(button.property("originalText"))
                        else:
                                # Show the original text
                                # Hide the text
                                button.setText('')
                                
                                
        else:
            print("toggle disabled")
            for button in self.frame_left_menu.findChildren(QPushButton):
                button.setStyleSheet("background-color: #2D2F31; color: white;")
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
def maximize_restore(self, ui):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            ui.btn_maximize_restore.setToolTip("Restore")
            ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            ui.btn_maximize_restore.setToolTip("Maximize")
            ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            ui.frame_size_grip.show()
def dobleClickMaximizeRestore(event, self, ui): 
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: maximize_restore(self, ui))
                print("double click")
def returStatus():
        return GLOBAL_STATE

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_close.clicked.connect(lambda: MainWindow.close())
    ui.btn_toggle_menu.clicked.connect(lambda: toggleMenu(ui, 500, True))
    ui.btn_maximize_restore.clicked.connect(lambda: maximize_restore(MainWindow, ui))
    ui.btn_minimize.clicked.connect(lambda: MainWindow.showMinimized())

    MainWindow.sizegrip = QSizeGrip(MainWindow)
    MainWindow.sizegrip.setStyleSheet("width: 20px; height: 20px; margin: 0px; padding: 0px;")
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui.frame_label_top_btns.mouseDoubleClickEvent = lambda event: dobleClickMaximizeRestore(event, MainWindow, ui)
    
    MainWindow.show()
    sys.exit(app.exec_())

