# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crossword.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from datetime import date
from datetime import datetime

class Ui_MainWindow(object):
    """This is the main window class that contains every widget,grid and answer that we display to the screen. It was generated using PyQt UI interface, so every change made in the interface is displayed here in code.
    """
    def setupUi(self, MainWindow, cellNumberArray, cellBlockArray, cluesAcross, cluesDown, cellAnswerArray, solved):
        MainWindow.setObjectName("LUMOS Puzzle Solver")
        MainWindow.resize(1127, 743)
        MainWindow.adjustSize()
        self.cellNumberArray = cellNumberArray
        self.cellBlockArray = cellBlockArray
        self.cluesAcross = cluesAcross
        self.cluesDown = cluesDown
        self.cellAnswerArray = cellAnswerArray
        self.solved = solved
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
    
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(131, 131, 131);\n"
"border-width: 1;\n"
"border-style: solid;")
        self.widget.setObjectName("widget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labels = {}
        self.gridList_1 = {}

        self.generateInitialGrid(MainWindow, self.cellBlockArray, self.widget, self.gridLayout_2, self.labels, self.gridList_1)
        self.revealAnswers(self.cellAnswerArray, self.labels)

        self.widget_right = QtWidgets.QWidget(self.frame_2)
        self.widget_right.setMinimumSize(QtCore.QSize(500, 500))
        self.widget_right.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(131, 131, 131);\n"
"border-width: 1;\n"
"border-style: solid;")
        self.widget_right.setObjectName("widget_right")
        self.widget_right.setSizePolicy(sizePolicy)

        self.gridLayout_right = QtWidgets.QGridLayout(self.widget_right)
        self.gridLayout_right.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_right.setSpacing(0)
        self.gridLayout_right.setObjectName("gridLayout_right")
        self.labels_2 = {}
        self.gridList_2 = {}

        self.generateInitialGrid(MainWindow, self.cellBlockArray, self.widget_right, self.gridLayout_right, self.labels_2, self.gridList_2)
        self.revealAnswers(self.solved, self.labels_2)

        self.horizontalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_3.setMinimumSize(500,500)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_3)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.widget_3)
        self.listWidget.setWordWrap(True)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 1, 1, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.gridLayout_3.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout_3.addWidget(self.label_55, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget_right)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_56 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setWordWrap(False)
        self.label_56.setObjectName("label_56")
        self.verticalLayout.addWidget(self.label_56)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def retranslateUi(self, MainWindow):
        """This method is also automatically generated in order to encode the text in the labels that we use, hence it takes a translate function. This function is called after the initial grids are generated.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lumos Puzzle Solver"))
        self.label.setText(_translate("MainWindow", "The Mini Crossword"))
        self.generateLabelNumbers(MainWindow, self.cellNumberArray, _translate, self.labels) #Generate numbers that will be displayed on the grid for the first grid.
        self.generateLabelNumbers(MainWindow, self.cellNumberArray, _translate, self.labels_2) #Generate numbers that will be displayed on the grid for the second grid.
        __sortingEnabled = self.listWidget.isSortingEnabled() 
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled) #Enable sorting for the clues so that the first clue starting with 1 is always on top.
        self.label_54.setText(_translate("MainWindow", "ACROSS"))
        self.label_55.setText(_translate("MainWindow", "DOWN"))

        self.generateClues(MainWindow, self.cluesAcross, self.cluesDown, _translate)
        self.label_56.setText(_translate("MainWindow", "Group LUMOS, Today\'s Date: {} {}".format(date.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"))))

    def generateInitialGrid(self, MainWindow, blackGrids, widgetName, input_grid, labels, gridList):
        """Generates the initial grid, creates frames and labels that we will fill later.

        Args:
            MainWindow ([type]): MainWindow that we will show the grid in.
            blackGrids (List): Information from the backend regarding which grids are black in todays puzzle.
            widgetName (Widget): Widget that the grid is bound to in the frame.
            input_grid (Dictionary): Grid dictionary that holds every label and every frame that made up the cells.
            labels (Dictionary): Label dictionary that holds the numbers and the colors of the grid cells.
        """
        for row in range(5):
            for col in range(5):
                # Establish grid and label names
                gridName = "frame_{}_{}".format(str(row), str(col))
                # Create a grid element
                gridList[gridName] = QtWidgets.QFrame(widgetName)
                # Set the tile color
                if blackGrids[row][col] == '1':
                    gridList[gridName].setStyleSheet("background-color: rgb(0, 0, 0);")
                else:
                    gridList[gridName].setStyleSheet("background-color: rgb(255,255,255);")

                # Set the frame shape
                gridList[gridName].setFrameShape(QtWidgets.QFrame.StyledPanel)
                # Set the frame shadow
                gridList[gridName].setFrameShadow(QtWidgets.QFrame.Raised)
                # Set object name
                gridList[gridName].setObjectName(gridName)

                # Create the labels for the tile, the first label in the tuple is the 
                labels[gridName] = (QtWidgets.QLabel(gridList[gridName]), QtWidgets.QLabel(gridList[gridName])) 
                
                # Set the styles of the labels
                labels[gridName][0].setGeometry(QtCore.QRect(20, 40, 60, 55))
                labels[gridName][1].setGeometry(QtCore.QRect(5, 10, 31, 31))
                font = QtGui.QFont()
                
                font.setFamily("Helvetica")
                font.setPointSize(36)
                font.setWeight(40)
                labels[gridName][0].setFont(font)

                font2 = QtGui.QFont()
                font2.setFamily("Arial")
                font2.setPointSize(20)
                font2.setWeight(30)
                labels[gridName][1].setFont(font2)

                labels[gridName][0].setStyleSheet("border-width: 0; color: rgb(40, 96, 216)")
                labels[gridName][1].setStyleSheet("border-width: 0")
                labels[gridName][0].setAlignment(QtCore.Qt.AlignCenter)
                input_grid.addWidget(gridList[gridName], row, col, 1, 1)

    def generateLabelNumbers(self, MainWindow, gridNumbers, translate, labels):
        """Numbers the grid cells according to today's puzzle. The number information comes from the backend and it is in list form.
        """
        for row in range(5):
            for col in range(5):
                if gridNumbers[row][col] != '-':
                    gridName = "frame_{}_{}".format(str(row), str(col))
                    labels[gridName][1].setText(translate(str(MainWindow), gridNumbers[row][col]))
    
    def generateClues(self, MainWindow, cluesAcross, cluesDown, translate):
        """Places today's clues inside a list in order to display it onto the page. Clues information come from backend.
        """
        for across in cluesAcross:
            item = QtWidgets.QListWidgetItem()
            self.listWidget_2.addItem(item)
            clue = "{} {} \n".format(str(across[0]), across[1])
            item.setText(translate(str(MainWindow), clue))
        for down in cluesDown:
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            clue = "{} {} \n".format(str(down[0]), down[1])
            item.setText(translate(str(MainWindow), clue))

    def revealAnswers(self, cellAnswerArray, labels):
        """ Displays the letters that corresponds to the answers in the cells.
        """
        for row in range(5):
            for col in range(5):
                if cellAnswerArray[row][col] != '-':
                    gridName = "frame_{}_{}".format(str(row), str(col))
                    labels[gridName][0].setText(cellAnswerArray[row][col])
