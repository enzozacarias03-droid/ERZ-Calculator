import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        #Configurando o layout basico
        #substituimos o window pelo self
        self.cw = QWidget()
        self.v_layout = QVBoxLayout() #tipo de layout
        self.cw.setLayout(self.v_layout) #tas a escolher o layout
        self.setCentralWidget(self.cw)

        #Titulo da janela
        self.setWindowTitle('ERZ Calculator')#meter titulo na janela

      
    def adjustFixedSize(self):
        #Ultima coisa a ser feita
        self.adjustSize() #ajustar tamanho da janela
        self.setFixedSize(self.width(), self.height()) 
        #tamanho fixo, que nao muda

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
        
        
      