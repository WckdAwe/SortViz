import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QDesktopWidget, QPushButton, \
    QInputDialog, QLineEdit, QGridLayout, QDialog, QMainWindow, QMessageBox ,QAction
from  PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore,QtWidgets
import pysort
import random

# test imports
from matplotlib import pyplot as plt
import matplotlib
from time import sleep
import warnings

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
fig = plt.figure()

def randomize():
    global a_list
    a_list = random.sample(range(150), 20)

def PopMsg(input):
    msg = QMessageBox()
    msg.setDefaultButton(QMessageBox.Ok)
    msg.setWindowTitle("Done!")
    msg.setText("Sorted List: "+str(input))
    msg.exec()
    
a_list = []  # just a random list
#randomize()

class window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Sorting Algorithms")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_C)

        self.menuBar().addMenu(self.file_menu)
        self.help_menu = QtWidgets.QMenu('&Help', self)

        self.menuBar().addSeparator()
        
        self.menuBar().addMenu(self.help_menu)
        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        self.main_widget.setFocus()

        self.setCentralWidget(self.main_widget)
        self.createGridLayout()
        
        self.windowLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.windowLayout.addWidget(self.horizontalGroupBox)

        self.show()

    def fileQuit(self):
        self.close()
        
    def closeEvent(self, ce):
        self.fileQuit()
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.createGridLayout()
        
        windowLayout = QVBoxLayout(self.main_widget)
        windowLayout.addWidget(self.horizontalGroupBox)

        self.show()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About","""===DA HANDSOMES===\nTaxiarhis\nNikos\nAris""")

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Press a button for visualization")
        layout = QGridLayout()
        layout.setColumnStretch(0, 5)
        layout.setColumnStretch(1, 5)
        layout.setColumnStretch(2, 5)

        # List buttons

        randomList = QPushButton("Random List / Clear Plot",self)
        randomList.setToolTip("Click to create a random list / Clear Plot")
        buttonCreateYourList = QPushButton("Create List", self)
        buttonCreateYourList.setToolTip("Click to create a custom list")
        showList = QPushButton("Show current list / Pause", self)                   # added by @Aris
        showList.setToolTip("Click to show the inputed List! or Pause")      # added by @Aris

        # Sorting Algorithms Buttons

        binaryInsertionButton = QPushButton("Binary Insetion Sort", self)
        binaryInsertionButton.setToolTip("Click for Binary Insertion sort visualization")
        bucketSortButton = QPushButton("Bucket Sort", self)
        bucketSortButton.setToolTip("Click for Bucket sort visualization")
        insertionSortButton = QPushButton("Insertion Sort*", self)
        insertionSortButton.setToolTip("Click for insertion sort visualization")
        selectionSortButton = QPushButton("Selection Sort*", self)
        selectionSortButton.setToolTip("Click for Selection sort visualization")
        mergeSortButton = QPushButton("Merge Sort", self)
        mergeSortButton.setToolTip("Click for Merge sort visualization")
        heapsortButton = QPushButton("Heap Sort", self)
        heapsortButton.setToolTip("Click for heapsort visualization")
        quicksortButton = QPushButton("Quick Sort", self)
        quicksortButton.setToolTip("Click for Quicksort visualization")
        bubbleSortButton = QPushButton("Bubble Sort*", self)
        bubbleSortButton.setToolTip("Click for Bubble sort visualization")
        shellsortButton = QPushButton("Shell Sort", self)
        shellsortButton.setToolTip("Click for shellsort visualization")
        combSortButton = QPushButton("Comb Sort", self)
        combSortButton.setToolTip("Click for Comb sort visualization")
        countingSortButton = QPushButton("Counting Sort*",self)
        countingSortButton.setToolTip("Click for Counting sort visualization")
        radixSortButton = QPushButton("Radix Sort", self)
        radixSortButton.setToolTip("Click for Radix sort visualization")
        radixSortButton.setEnabled(False)   # added by @Aris
        timsortButton = QPushButton("Tim Sort", self)
        timsortButton.setToolTip("Click for Timsort  visualization")
        cycleButton = QPushButton("Cycle Sort", self)
        cycleButton.setToolTip("Click for Cycle sort visualization")
        cocktailButton = QPushButton("Cocktail Sort*", self)
        cocktailButton.setToolTip("Click for Cocktail sort visualization")
        bitonicButton = QPushButton("Bitonic Sort", self)
        bitonicButton.setToolTip("Click for Bitonic sort visualization")
        pancakeButton = QPushButton("Pancake Sort", self)
        pancakeButton.setToolTip("Click for Pancake sort visualization")
        bogosortButton = QPushButton("Bogo Sort*", self)
        bogosortButton.setToolTip("Click for Bogosort visualization")
        gnomeSortButton = QPushButton("Gnome Sort*", self)
        gnomeSortButton.setToolTip("Click for Gnome sort visualization")
        sleepSortButton = QPushButton("Sleep Sort", self)
        sleepSortButton.setToolTip("Click for Sleep sort visualization")
        stoogeButton = QPushButton("Stooge Sort", self)
        stoogeButton.setToolTip("Click for Stooge sort visualization")

        layout.addWidget(buttonCreateYourList, 0, 0)
        layout.addWidget(randomList, 0, 1)
        layout.addWidget(showList, 0, 2)            # added by @Aris
        layout.addWidget(insertionSortButton, 1, 0)
        layout.addWidget(selectionSortButton, 1, 1)
        layout.addWidget(gnomeSortButton, 1, 2)
        layout.addWidget(heapsortButton, 2, 0)
        layout.addWidget(quicksortButton, 2, 1)
        layout.addWidget(mergeSortButton, 2, 2)
        layout.addWidget(shellsortButton, 3, 0)
        layout.addWidget(combSortButton, 3, 1)
        layout.addWidget(bubbleSortButton, 3, 2)
        layout.addWidget(bogosortButton, 4, 0)
        layout.addWidget(radixSortButton, 4, 1)
        layout.addWidget(bucketSortButton, 4, 2)
        layout.addWidget(stoogeButton, 5, 0)
        layout.addWidget(cycleButton, 5, 1)
        layout.addWidget(timsortButton, 5, 2)
        layout.addWidget(bitonicButton, 6, 0)
        layout.addWidget(pancakeButton, 6, 1)
        layout.addWidget(cocktailButton, 6, 2)
        layout.addWidget(countingSortButton,7,0)
        layout.addWidget(sleepSortButton, 7, 1)
        layout.addWidget(binaryInsertionButton, 7, 2)

        # What buttons do when clicked:

        buttonCreateYourList.clicked.connect(self.createCustomList)
        randomList.clicked.connect(self.random_list)
        showList.clicked.connect(self.show_list)
        insertionSortButton.clicked.connect(self.InsertionAlgo)
        selectionSortButton.clicked.connect(self.SelectionAlgo)
        mergeSortButton.clicked.connect(self.MergeAlgo)
        heapsortButton.clicked.connect(self.HeapAlgo)
        quicksortButton.clicked.connect(self.QuicksortAlgo)
        bubbleSortButton.clicked.connect(self.BubbleAlgo)
        shellsortButton.clicked.connect(self.ShellAlgo)
        combSortButton.clicked.connect(self.CombAlgo)
        countingSortButton.clicked.connect(self.CountingAlgo)
        bucketSortButton.clicked.connect(self.BucketAlgo)
        radixSortButton.clicked.connect(self.RadixAlgo)
        timsortButton.clicked.connect(self.TimsortAlgo)
        cycleButton.clicked.connect(self.CycleAlgo)
        cocktailButton.clicked.connect(self.CocktailAlgo)
        bitonicButton.clicked.connect(self.BitonicAlgo)
        pancakeButton.clicked.connect(self.PancakeAlgo)
        binaryInsertionButton.clicked.connect(self.BinaryInsertionAlgo)
        bogosortButton.clicked.connect(self.BogosortAlgo)
        gnomeSortButton.clicked.connect(self.GnomeAlgo)
        sleepSortButton.clicked.connect(self.SleepAlgo)
        stoogeButton.clicked.connect(self.StoogeAlgo)

        self.horizontalGroupBox.setLayout(layout)

        # Code to execute when buttons clicked :

    @pyqtSlot()
    def InsertionAlgo(self):
        temp= a_list.copy()
        temp = pysort.insertion_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def SelectionAlgo(self):
        temp = a_list.copy()
        temp = pysort.selection_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def MergeAlgo(self):
        temp = a_list.copy()
        temp = pysort.merge_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def HeapAlgo(self):
        temp = a_list.copy()
        temp = pysort.heap_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def QuicksortAlgo(self):
        temp = a_list.copy()
        temp = pysort.quicksort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def BubbleAlgo(self):
        temp = a_list.copy()
        temp = pysort.bubble_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def ShellAlgo(self):
        temp = a_list.copy()
        temp = pysort.shell_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def CombAlgo(self):
        temp = a_list.copy()
        temp = pysort.comb_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def CountingAlgo(self):
        temp = a_list.copy()
        temp = pysort.counting_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def BucketAlgo(self):
        temp = a_list.copy()
        temp = pysort.bucket_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def RadixAlgo(self):
        temp = a_list.copy()
        temp = pysort.radix_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def TimsortAlgo(self):
        temp = a_list.copy()
        temp = pysort.timsort(temp, fig)
        PopMsg(temp)
        print(a_list)

    @pyqtSlot()
    def CycleAlgo(self):
        temp = a_list.copy()
        temp = pysort.cycle_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def CocktailAlgo(self):
        temp = a_list.copy()
        temp = pysort.cocktail_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def BitonicAlgo(self):
        temp = a_list.copy()
        temp = pysort.bitonic_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def PancakeAlgo(self):
        temp = a_list.copy()
        temp = pysort.pancake_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def BinaryInsertionAlgo(self):
        temp = a_list.copy()
        temp = pysort.binary_insertion_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def BogosortAlgo(self):
        temp = a_list.copy()
        temp = pysort.bogosort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def GnomeAlgo(self):
        temp = a_list.copy()
        temp = pysort.gnome_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def SleepAlgo(self):
        temp = a_list.copy()
        temp = pysort.sleep_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def StoogeAlgo(self):
        temp = list(a_list)
        temp = pysort.stooge_sort(temp, fig)
        PopMsg(temp)
        print(temp)

    @pyqtSlot()
    def random_list(self):
        randomize()
        plt.clf()

    @pyqtSlot()
    def createCustomList(self):  # THIS WILL CHANGE AFTER THE REWORK!!!!!
        text, okPressed = QInputDialog.getText(self, "Custom List", "Type your list(separate numbers with comma):",
                                               QLineEdit.Normal, "")
        text += ','
        newText = ""
        number = ""
        global a_list
        a_list = []
        for item in text:

            if item != ' ':
                newText = newText + item

        try:
            for item in newText:

                if item != ',':
                    number += item
                else:
                    a_list.append(int(number))
                    number = ""
            plt.clf()
        except ValueError:
            print("ERROR!")  # NEED TO FIX THIS PART

    # added by @Aris
    @pyqtSlot()
    def show_list(self):
        QMessageBox.about(self, "Your Inputed List", str(a_list))




def run():
    qApp = QtWidgets.QApplication(sys.argv)
    aw = window()
    aw.show()
    sys.exit(qApp.exec_())
    
    #app = QApplication(sys.argv)
    #prog = window()
    #sys.exit(app.exec_())


run()

#    def __init__(self):
#         super().__init__()
#         self.title = "Algoriths Visualization"
#         self.width = 640
#         self.height = 480
#         self.top = 10
#         self.left = 10

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)
#         self.center()
#         self.createGridLayout()

#         windowLayout = QVBoxLayout()
#         windowLayout.addWidget(self.horizontalGroupBox)
#         self.setLayout(windowLayout)
#         self.show()

#     # center window to the screen
#     def center(self):

#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
