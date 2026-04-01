import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        #Configuring the basic layout
        #substituing window for self
        self.cw = QWidget()
        self.v_layout = QVBoxLayout() #type of layout
        self.cw.setLayout(self.v_layout) #choosing the layout
        self.setCentralWidget(self.cw)

        #Window title
        self.setWindowTitle('ERZ Calculator')#Putting the title on the window

      
    def adjustFixedSize(self):
        #Last thing to be done
        self.adjustSize() #Adjusting window size
        self.setFixedSize(self.width(), self.height()) 
        #Fixed size that does not change

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
        
        
      